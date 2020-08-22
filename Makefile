
BUILD = svgbob

all: svgbob

init:
	mkdir -p $(BUILD)

svgbob: init
	@echo "svgbob"
	docker run --rm -it -v $(PWD):/tmp -w /tmp joseluisq/rust-linux-darwin-builder ./cargo.sh

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
