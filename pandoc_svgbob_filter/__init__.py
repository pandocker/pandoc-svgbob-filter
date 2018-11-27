import panflute as pf


class SvgbobInline(object):
    def action(self, elem, doc):
        return elem


def main(doc=None):
    si = SvgbobInline()
    pf.run_filters([si.action], doc=doc)
    return doc


if __name__ == "__main__":
    main()
