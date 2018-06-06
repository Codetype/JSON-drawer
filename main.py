from optparse import OptionParser
from Drawing.Parser import Parser
from Drawing import Drawer
import sys

def main(argv):
    if len(argv) < 2:
        print("Not enough arguments. You should set <input.json> (and to save picture) <-o or --output> <output.png>")
        return
    else:
        opt_parser = OptionParser()
        opt_parser.add_option("-o", "--output", dest="dest", help="creating output file png with creating shapes", metavar="DEST")
        (options, args) = opt_parser.parse_args()

        input_json = args[0]
        output_image = vars(options)['dest']

        if Parser.check_input(args[0]):
            parsed_file = Parser(input_json)

            img_flag = True
            if not output_image:
                img_flag = False
            elif not Parser.check_output(output_image):
                img_flag = False

            Drawer.draw_figures(parsed_file, output_image, img_flag)

if __name__ == '__main__':
   main(sys.argv)