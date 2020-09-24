import m2r
import re
import os


def make_rst_file(md_file_path):

    rst_file_name = os.path.split(md_file_path)[1].replace('.md', '.rst')
    rst_file_path = os.path.join('../../docs', rst_file_name)

    file_contents = m2r.convert(open(md_file_path).read())
    with open(rst_file_path, 'w') as file:
        file.write(file_contents)
    return rst_file_path


def make_tocs():

    tree = list(os.walk('../../writing/markdown/'))

    all_tocs = "    Contents:\n"
    toc_template = """
    .. toctree::
       :maxdepth: 2
       :caption: {caption}"""

    subdirs = {t[0]: sorted([f for f in t[2] if f.endswith('md')])for t in tree[1:]}
    toc_headings = sorted(list(subdirs.keys()))

    for path in toc_headings:
        caption = re.sub('[0-9]?\.', '', os.path.split(path)[1])

        toc = toc_template.format(caption=caption) + "\n\n"

        for md_file in subdirs[path]:
            md_path = os.path.join(path, md_file)
            rst_file = make_rst_file(md_path)
            toc += " "*7 + f"{os.path.split(rst_file)[1].replace('.rst', '')}\n"

        all_tocs += f"\n{toc}\n"

    return strip_leading_4_chars(all_tocs)


def make_after_toc():
    return strip_leading_4_chars("""
    .. toctree::
       :maxdepth: 2
       :caption: Help and Reference

       GitHub Repo <https://github.com/luke-gregor/test_publication>



    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`
    """)


def strip_leading_4_chars(string):
    return '\n'.join([s[4:] for s in string.split('\n')])


def make_index_rst():

    part1 = m2r.convert(open('../../README.md').read())

    part2 = make_tocs()

    part3 = make_after_toc()

    index_rst = f"{part1}\n{part2}\n{part3}"

    with open('../../docs/index.rst', 'w') as file:
        file.write(index_rst)


if __name__ == "__main__":
    __directory__ = os.path.dirname(os.path.abspath(__file__))
    os.chdir(__directory__)

    make_index_rst()
