
BUILD = svgbob

all: svgbob

init:
	mkdir -p $(BUILD)

svgbob: init
	echo "svgbob"
	docker run --rm -v $(PWD):/tmp -w /tmp rust cargo install svgbob_cli --root=$(BUILD)
#	cargo install svgbob_cli --root=$(BUILD)

initdir:
	cd tests && make initdir
html:
	cd tests && make html
pdf:
	cd tests && make pdf

clean:
	rm -rf $(BUILD)/bin/svgbob
