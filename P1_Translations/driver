#!/usr/bin/env python3

from translation_project import *

def main():
    font_file = 'fonts.txt'
    font_path = 'text_src_files/' + font_file
    full_font_path = Path(font_path)
    trans_dict = build_translator(full_font_path, get_lang_keys(full_font_path))

    directives_file = 'directives.txt'
    directives_path = 'text_src_files/' + directives_file
    full_directives_path = Path(directives_path)
    directives_ = parse_directives(full_directives_path)
    run_directives(trans_dict, directives_)


main()