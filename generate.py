import logging
import argparse

from ocgenerator import OCGenerator, read_config, ensure_config


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--framework')
    group.add_argument('--toolkit')
    group.add_argument('--module')
    args = parser.parse_args()
    config = ensure_config(read_config())
    generator = OCGenerator(config)
    generator.write_version()
    if args.framework:
        generator.process_framework(args.toolkit)
    elif args.toolkit:
        generator.process_toolkit(args.toolkit)
    elif args.module:
        generator.process_module(args.module)
    else:
        generator.process_everything()
