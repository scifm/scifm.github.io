# SciFM Website Makefile

# Targets that aren't filenames
.PHONY: all install build test serve clean publications help

all: install build test

install: install-python
	bundle install

install-python:
	uv sync

build: publications
	JEKYLL_ENV=production bundle exec jekyll build

test: build
	bundle exec htmlproofer --disable-external --ignore-missing-alt _site

# Generate publication markdown files from BibTeX
publications: _publications/
_publications/: publications.bib bib2jekyll.py
	@echo "Generating publications from BibTeX..."
	uv run python bib2jekyll.py publications.bib _publications
	@touch $@

# Serve locally for development
SERVE_HOST ?= 127.0.0.1
SERVE_PORT ?= 4000

serve: publications
	bundle exec jekyll serve --livereload

# Clean build artifacts
clean:
	$(RM) -r _site _publications/*.md
	@echo "Cleaned _site and publication files"
	touch publications.bib

# Show help
help:
	@echo "SciFM Website Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  make all           - Install, build, and test (default)"
	@echo "  make install       - Install dependencies (Ruby + Python)"
	@echo "  make build         - Build the site for production"
	@echo "  make test          - Run site tests"
	@echo "  make serve         - Serve locally for development (port 4000)"
	@echo "  make publications  - Regenerate publications from BibTeX"
	@echo "  make clean         - Remove build artifacts"
	@echo ""
	@echo "Configuration:"
	@echo "  SERVE_HOST=0.0.0.0 make serve  - Serve on all interfaces"
	@echo "  SERVE_PORT=5000 make serve     - Serve on custom port"