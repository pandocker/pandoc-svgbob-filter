
BUILD = svgbob

all: svgbob

init:
	mkdir -p $(BUILD)

svgbob: init
	echo "svgbob"
	cargo install svgbob_cli --root=$(BUILD)

clean:
	rm -rf $(BUILD)/bin/svgbob
