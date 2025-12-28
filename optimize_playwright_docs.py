#!/usr/bin/env python3
"""
Optimize Playwright documentation files for LLM inference by:
1. Removing Python documentation links
2. Removing version tags
3. Converting web links to local file references
4. Fixing escaped underscores
"""

import re
from pathlib import Path

def optimize_markdown(content: str) -> str:
    """Apply optimizations to markdown content."""
    
    # Remove escaped underscores (fix \_ to _)
    content = re.sub(r'\\_', '_', content)
    
    # Remove Python doc links but keep the type text
    # Pattern: [str](https://docs.python.org/...) -> str
    content = re.sub(
        r'\[([^\]]+)\]\(https://docs\.python\.org/[^\)]+\)',
        r'\1',
        content
    )
    
    # Remove pathlib.Path links from realpython.com
    content = re.sub(
        r'\[pathlib\.Path\]\(https://realpython\.com/[^\)]+\)',
        r'pathlib.Path',
        content
    )
    
    # Remove version tags like "Added in: v1.16" or "Added in: 1.46"
    # These appear on their own lines or inline
    content = re.sub(
        r'\s*Added in:\s*v?\d+\.\d+\s*',
        ' ',
        content
    )
    
    # Remove anchor links like [#](#some-anchor)
    content = re.sub(
        r'\[\#\]\([^\)]+\)',
        '',
        content
    )
    
    # Convert Playwright class links to local file references
    # [ClassName](/python/docs/api/class-name) -> [ClassName](ClassName.md)
    def convert_class_link(match):
        class_name = match.group(1)
        class_slug = match.group(2).replace('class-', '')
        
        # Handle special capitalization cases
        special_cases = {
            'jshandle': 'JSHandle',
            'apirequest': 'APIRequest',
            'apirequestcontext': 'APIRequestContext',
            'apiresponse': 'APIResponse',
            'apiresponseassertions': 'APIResponseAssertions',
            'cdpsession': 'CDPSession',
        }
        
        if class_slug in special_cases:
            filename = special_cases[class_slug]
        else:
            # Convert kebab-case to PascalCase
            parts = class_slug.split('-')
            filename = ''.join(word.capitalize() for word in parts)
        
        return f'[{class_name}]({filename}.md)'
    
    content = re.sub(
        r'\[([^\]]+)\]\(/python/docs/api/(class-[a-z-]+)[^\)]*\)',
        convert_class_link,
        content
    )
    
    # Remove "On this page" sections
    content = re.sub(
        r'On this page\n\n',
        '',
        content
    )
    
    # Remove bottom navigation (Methods list with links)
    content = re.sub(
        r'\n\* \[Methods\]\(#[^\)]+\).*$',
        '',
        content,
        flags=re.MULTILINE | re.DOTALL
    )
    
    # Clean up multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip() + '\n'


def process_file(filepath: Path) -> None:
    """Process a single markdown file."""
    print(f"Processing {filepath.name}...")
    
    content = filepath.read_text(encoding='utf-8')
    optimized = optimize_markdown(content)
    
    # Only write if content changed (idempotent check)
    if content != optimized:
        filepath.write_text(optimized, encoding='utf-8')
        print(f"  ✓ Optimized {filepath.name}")
    else:
        print(f"  • Skipped {filepath.name} (already optimized)")


def main():
    """Process all markdown files in the playwright_python_classes directory."""
    docs_dir = Path('agent/skills/playwright/playwright_python_classes')
    
    if not docs_dir.exists():
        print(f"Error: Directory not found: {docs_dir}")
        return
    
    md_files = sorted(docs_dir.glob('*.md'))
    
    if not md_files:
        print(f"No markdown files found in {docs_dir}")
        return
    
    print(f"Found {len(md_files)} markdown files to optimize\n")
    
    optimized_count = 0
    skipped_count = 0
    
    for filepath in md_files:
        try:
            content_before = filepath.read_text(encoding='utf-8')
            process_file(filepath)
            content_after = filepath.read_text(encoding='utf-8')
            
            if content_before != content_after:
                optimized_count += 1
            else:
                skipped_count += 1
        except Exception as e:
            print(f"  ✗ Error processing {filepath.name}: {e}")
    
    print(f"\n✅ Completed! Optimized {optimized_count} files, skipped {skipped_count} files (already optimal).")


if __name__ == '__main__':
    main()
