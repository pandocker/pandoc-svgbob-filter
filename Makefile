
BUILD = svgbob

all: svgbob

init:
	mkdir -p $(BUILD)

svgbob: init
	echo "svgbob"
#	docker run --rm -v $(PWD):/tmp -w /tmp rust cargo install svgbob_cli --root=$(BUILD) --target=x86_64-unknown-linux-musl
	docker run --rm -it -v $(PWD):/tmp -w /tmp rust ./cargo.sh
#	cargo install svgbob_cli --root=$(BUILD)

initdir:
	cd tests && make initdir

html:
	cd tests && make html

docx:
	cd tests && make docx

tex:
	cd tests && make tex

pdf:
	cd tests && make pdf

clean:
	cd tests && make clean
#	rm -rf $(BUILD)/bin/svgbob
