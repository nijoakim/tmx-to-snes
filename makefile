SOURCE=tmx-to-snes $(wildcard *.py)

.PHONY: all
all: build

.PHONY: clean
clean:
	rm -rf build

.PHONY: build
build: | build/

.PHONY: install
install: build
	./setup.py install

build/: $(SOURCE)
	@touch -c build
	./setup.py build
