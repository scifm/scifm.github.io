#!/usr/bin/env python3
"""Convert BibTeX to Jekyll markdown files."""

import bibtexparser
import sys
import re
from pathlib import Path


def clean_text(text):
    """Remove LaTeX braces and clean text."""
    return text.replace('{', '').replace('}', '').strip()


def entry_to_markdown(entry):
    """Convert BibTeX entry to markdown with YAML front matter."""
    title = clean_text(entry.get('title', ''))
    year = entry.get('year', '')
    journal = entry.get('journal', '')
    url = entry.get('url', '')
    
    # Venue
    if 'arXiv' in journal:
        venue = 'arXiv'
    elif journal:
        venue = clean_text(journal)
    else:
        venue = 'Preprint'
    
    # Authors for citation
    authors = entry.get('author', '').replace(' and ', ', ')
    
    # Build YAML
    yaml = f"""---
title: "{title}"
collection: publications
date: {year}-01-01
venue: '{venue}'
paperurl: '{url}'
authors: '{authors}'
---
"""
    return yaml


def main():
    if len(sys.argv) != 3:
        print("Usage: python bib2jekyll.py input.bib output_dir")
        sys.exit(1)
    
    bib_file = sys.argv[1]
    output_dir = Path(sys.argv[2])
    output_dir.mkdir(exist_ok=True)
    
    # Parse BibTeX
    with open(bib_file, 'r') as f:
        bib = bibtexparser.load(f)
    
    # Convert each entry
    for i, entry in enumerate(bib.entries, 1):
        year = entry.get('year', '0000')
        title_slug = re.sub(r'[^\w\s-]', '', entry.get('title', '')[:30].lower())
        title_slug = re.sub(r'[-\s]+', '-', title_slug).strip('-')
        
        filename = f"{year}-{title_slug}.md"
        content = entry_to_markdown(entry)
        
        (output_dir / filename).write_text(content)
        print(f"{i}. {filename}")
    
    print(f"\nCreated {len(bib.entries)} files in {output_dir}/")


if __name__ == '__main__':
    main()
