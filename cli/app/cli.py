from argparse import ArgumentParser


def main():
    parser = ArgumentParser(prog='cli')
    parser.add_argument(
        'login', help="For authentication and logging in"
    )
    parser.add_argument(
        '--name', help="For authentication and logging in"
    )
    args = parser.parse_args()
    print("Hello, %s!" % args.name)


if __name__ == '__main__':
    main()
