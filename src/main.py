import cli

def main():
    parser = cli.build_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
   