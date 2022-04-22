import unittest
from translation_project import *

class testFontsMixedTranslation(unittest.TestCase):

    def setUp(self) -> None:
        '''
        Creates the translated files so we can test the output
        :return: None
        '''
        curr_dirr = os.getcwd()
        curr_dirr = curr_dirr.rstrip('test')

        font_file = 'fontsmixed.txt'
        font_path = 'text_src_files/' + font_file
        full_font_path = Path(curr_dirr + font_path)
        trans_dict = build_translator(full_font_path, get_lang_keys(full_font_path))

        directives_file = 'directives.txt'
        directives_path = 'text_src_files/' + directives_file
        full_directive_path = Path(curr_dirr + directives_path)
        directives_ = parse_directives(full_directive_path)
        run_directives(trans_dict, directives_, isTest=True)

    def test_english_to_morse(self):
        with open('out1.txt', mode='r') as translated:
            translation = translated.readline()

        expected = '-. --- .-- / .. ... / - .... . / - .. -- . ' \
                   '/ ..-. --- .-. / .- .-.. .-.. / --. --- --- -.. ' \
                   '/ -.. --- --. ... / - --- / -.-. --- -- . / - --- ' \
                   '/ - .... . / .- .. -.. / --- ..-. / - .... . .. .-. ' \
                   '/ --- .-- -. . .-. ... -.-.-- ' + '\n'
        self.assertEqual(expected, translation)

    def test_english_to_phonetic(self):
        with open('out2.txt', mode='r') as translated:
            translation = translated.readline()

        expected = 'NOVEMBER OSCAR WHISKEY / INDIA SIERRA / TANGO HOTEL ECHO' \
                   ' / TANGO INDIA MIKE ECHO / FOXTROT OSCAR ROMEO / ALPHA LIMA ' \
                   'LIMA / GOLF OSCAR OSCAR DELTA / DELTA OSCAR GOLF SIERRA / ' \
                   'TANGO OSCAR / CHARLIE OSCAR MIKE ECHO / TANGO OSCAR / TANGO ' \
                   'HOTEL ECHO / ALPHA INDIA DELTA / OSCAR FOXTROT / TANGO HOTEL ' \
                   'ECHO INDIA ROMEO / OSCAR WHISKEY NOVEMBER ECHO ROMEO SIERRA ' \
                   'BANG ' + '\n'
        self.assertEqual(expected, translation)

    def test2_multi_lines_english_to_morse(self):
        with open('morseStar.txt', mode='r') as translated:
            translation = ''
            for line in translated.readlines():
                translation += line

        expected = '.... . -.-- / -. --- .-- --..-- / -.-- --- ..- ' \
                   '.----. .-. . / .- -. / .- .-.. .-.. / ... - .- .-. ' \
                   '--..-- / --. . - / -.-- --- ..- .-. / --. .- -- . / ' \
                   '--- -. --..-- / --. --- / .--. .-.. .- -.-- ' + '\n' + \
                   '.... . -.-- / -. --- .-- / -.-- --- ..- .----. .-. . ' \
                   '/ .- / .-. --- -.-. -.- / ... - .- .-. --..-- / --. . - ' \
                   '/ - .... . / ... .... --- .-- / --- -. --..-- / --. . - ' \
                   '/ .--. .- .. -.. ' + '\n' + \
                   '.- .-.. .-.. / - .... .- - / --. .-.. .. - - . .-. ... / ..' \
                   ' ... / --. --- .-.. -.. ' + '\n' + \
                   '--- -. .-.. -.-- / ... .... --- --- - .. -. --. / ... - .- ' \
                   '.-. ... / -... .-. . .- -.- / - .... . / -- --- .-.. -.. ' + '\n'
        self.assertEqual(expected, translation)

    def test_multi_line_english_to_phonetic(self):
        with open('phoneticStar.txt', mode='r') as translated:
            translation = ''
            for line in translated.readlines():
                translation += line

        expected = 'HOTEL ECHO YANKEE / NOVEMBER OSCAR WHISKEY COMMA / YANKEE OSCAR ' \
                   'UNIFORM APOSTROPHE ROMEO ECHO / ALPHA NOVEMBER / ALPHA LIMA LIMA / ' \
                   'SIERRA TANGO ALPHA ROMEO COMMA / GOLF ECHO TANGO / YANKEE OSCAR ' \
                   'UNIFORM ROMEO / GOLF ALPHA MIKE ECHO / OSCAR NOVEMBER COMMA / ' \
                   'GOLF OSCAR / PAPA LIMA ALPHA YANKEE ' + '\n' + \
                   'HOTEL ECHO YANKEE / NOVEMBER OSCAR WHISKEY / YANKEE OSCAR UNIFORM' \
                   ' APOSTROPHE ROMEO ECHO / ALPHA / ROMEO OSCAR CHARLIE KILO / SIERRA' \
                   ' TANGO ALPHA ROMEO COMMA / GOLF ECHO TANGO / TANGO HOTEL ECHO / SIERRA' \
                   ' HOTEL OSCAR WHISKEY / OSCAR NOVEMBER COMMA / GOLF ECHO TANGO / ' \
                   'PAPA ALPHA INDIA DELTA ' + '\n' + \
                   'ALPHA LIMA LIMA / TANGO HOTEL ALPHA TANGO / GOLF LIMA INDIA ' \
                   'TANGO TANGO ECHO ROMEO SIERRA / INDIA SIERRA / GOLF OSCAR ' \
                   'LIMA DELTA ' + '\n' + \
                   'OSCAR NOVEMBER LIMA YANKEE / SIERRA HOTEL OSCAR OSCAR TANGO ' \
                   'INDIA NOVEMBER GOLF / SIERRA TANGO ALPHA ROMEO SIERRA / BRAVO ' \
                   'ROMEO ECHO ALPHA KILO / TANGO HOTEL ECHO / MIKE OSCAR LIMA DELTA ' + '\n'
        self.assertEqual(expected, translation)


if __name__ == '__main__':
    unittest.main(verbosity=3)
