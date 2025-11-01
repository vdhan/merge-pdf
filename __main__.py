import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from datetime import date
from pathlib import Path

from pypdf import PdfWriter


def get_year(year: int) -> str:
    current: int = date.today().year
    return f'{year} - {current}' if current > year else f'{year}'


if __name__ == '__main__':
    parser = ArgumentParser(
        description='Ghép các file PDF',
        epilog=f'Bản quyền © {get_year(2025)} Vũ Đắc Hoàng Ân',
        formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument('-v', '--version', action='version', version='PDF merger 1.0.0')
    parser.add_argument('pdfs', nargs='+', help='Đường dẫn file pdf cần gộp', metavar='file.pdf')
    parser.add_argument('-o', default='đã gộp.pdf', help='Đường dẫn file pdf đã gộp', metavar='str')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    args = parser.parse_args()
    pdfs: list[str] = args.pdfs
    merger = PdfWriter()
    for pdf in pdfs:
        path = Path(pdf)
        if path.is_file():
            merger.append(pdf)
        else:
            print(f'Lỗi: {pdf} không phải là file')
            merger.close()
            sys.exit(1)

    merger.write(args.o)
    merger.close()
    print('Hoàn thành!')
