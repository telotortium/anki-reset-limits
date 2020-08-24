.PHONY: all clean
all: anki-reset-limits.ankiaddon
anki-reset-limits.ankiaddon:
	zip -r $@ $$(git ls-files | grep -v ^Makefile$$)
clean:
	rm -f anki-reset-limits.ankiaddon
