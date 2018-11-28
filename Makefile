
BUILD = svgbob

all: svgbob

init:
	mkdir -p $(BUILD)

svgbob: init
	echo "svgbob"
	docker run --rm -v $(PWD):/tmp -w /tmp rust cargo install svgbob_cli --root=$(BUILD)
#	cargo install svgbob_cli --root=$(BUILD)

clean:
	rm -rf $(BUILD)/bin/svgbob
