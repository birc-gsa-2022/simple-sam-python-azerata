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
        print(read_name.strip(), chrom.strip(), int(pos.strip())+1,
              f'{len(read_str)}M', read_str.strip(), sep='\t', end='\n')


if __name__ == '__main__':
    main()
