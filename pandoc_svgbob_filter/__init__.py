#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib
import subprocess as sp
import panflute as pf
from shutil import which


class SvgbobInline(object):
    """
    Converts alone Link in svgbob class to Image
    requires `svgbob` in PATH
    option can be provided as attributes or can set default values in yaml metadata block

    option          | metadata              | default
    ----------------|-----------------------|----------
    font-family     | svgbob.font-family    | "Arial"
    font-size       | svgbob.font-size      | 14
    scale           | svgbob.scale          | 1
    stroke_width    | svgbob.stroke-width   | 2

    """

    def __init__(self):
        self.dir_to = "svg"
        assert which("svgbob"), "svgbob is not in path"

    def action(self, elem, doc):
        if isinstance(elem, pf.Link) and "svgbob" in elem.classes:
            fn = elem.url
            options = elem.attributes
            caption = elem.content

            meta_font_family = doc.get_metadata("svgbob.font-family", "Arial")
            meta_font_size = doc.get_metadata("svgbob.font-size", 14)
            meta_scale = doc.get_metadata("svgbob.scale", 1)
            meta_stroke_width = doc.get_metadata("svgbob.stroke-width", 2)

            font_family = options.get("font-family", meta_font_family)
            font_size = options.get("font-size", meta_font_size)
            scale = options.get("scale", meta_scale)
            stroke_width = options.get("stroke-width", meta_stroke_width)
            svgbob_option = " ".join([
                '--font-family "{}"'.format(font_family) if font_family is not None else "",
                "--font-size {}".format(font_size) if font_size is not None else "",
                "--scale {}".format(scale) if scale is not None else "",
                "--stroke-width {}".format(stroke_width) if stroke_width is not None else "",
            ])
            if not os.path.exists(self.dir_to):
                os.mkdir(self.dir_to)

            data = open(fn, "r", encoding="utf-8").read()
            counter = hashlib.sha1(data.encode("utf-8")).hexdigest()[:8]
            self.basename = "/".join([self.dir_to, str(counter)])

            _format = "svg"
            # if doc.format in ["latex"]:
            #     format = "pdf"
            # elif doc.format in ["html", "html5"]:
            #     format = "svg"
            # else:
            #     format = "png"

            fn = os.path.abspath(fn)
            linkto = os.path.abspath(".".join([self.basename, _format])).replace("\\", "/")

            command = "svgbob {} {} -o {}".format(fn, svgbob_option, linkto)
            pf.debug(command)
            sp.Popen(command, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)

            pf.debug("[inline] generate svgbob from {} to {}".format(fn, linkto))
            elem.classes.remove("svgbob")
            elem = pf.Image(*caption, classes=elem.classes, url=linkto,
                            identifier=elem.identifier, title="fig:", attributes=elem.attributes)

            # pf.debug(elem)

            return elem


def main(doc=None):
    si = SvgbobInline()
    pf.run_filters([si.action], doc=doc)
    return doc


if __name__ == "__main__":
    main()
