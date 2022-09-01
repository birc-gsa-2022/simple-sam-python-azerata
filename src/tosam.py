import argparse


def main():
    argparser = argparse.ArgumentParser(description="To Simple-SAM converter")
    argparser.add_argument(
        "mas",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    for line in args.mas:
        chrom, read_name, read_str, pos = line.split('\t')
        print(f'{read_name}\t{chrom}\t{pos}\t{len(read_str)}M\t{read_str}')


if __name__ == '__main__':
    main()
