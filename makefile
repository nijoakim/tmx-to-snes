SOURCE=$(wildcard *.py)

all: build

clean:
	rm -rf build

build: $(SOURCE)
	./setup.py build

install: build
	./setup.py install
