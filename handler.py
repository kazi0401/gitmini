import argparse 

def build_parser() -> argparse.ArgumentParser: 
    parser = argparse.ArgumentParser(
        prog = "GitMini",
        description = "A simplified, introduction to Git"
    )

    parser.add_subparsers()





    return parser