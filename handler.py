import argparse 
import commands


def build_parser() -> argparse.ArgumentParser: 
    parser = argparse.ArgumentParser(
        prog = "GitMini",
        description = "A simplified, introduction to Git"
    )

    subparsers = parser.add_subparsers()

    # init command
    init_parser = subparsers.add_parser('init')
    init_parser.set_defaults(
        run_command = commands.init.run
    )
    
    # commit command
    commit_parser = subparsers.add_parser('commit')
    commit_parser.add_argument(
        '-m', '--message', 
        type = str,
        help = '')
    commit_parser.set_defaults(
        run_command = commands.commit.run
    )

    # checkout command
    checkout_parser = subparsers.add_parser('checkout')
    checkout_parser.add_argument(
        'commit_hash',
        type = str,
        help = ''
    )
    checkout_parser.set_defaults(
        run_command = commands.checkout.run
    )

    # log command
    log_parser = subparsers.add_parser('log')
    log_parser.set_defaults(
        run_command = commands.log.run
    )

    # tree command
    tree_parser = subparsers.add_parser('tree')
    tree_parser.add_argument(
        'commit_hash',
        type = str,
        help = ''
    )
    tree_parser.set_defaults(
        run_command = commands.tree.run
    )

    # diff command
    diff_parser = subparsers.add_parser('diff')
    diff_parser.add_argument(
        'commit_hash_A',
        type = str,
        help = ''
    )
    diff_parser.add_argument(
        'commit_hash_B',
        type = str,
        help = ''
    )
    diff_parser.set_defaults(
        run_command = commands.diff.run
    )

    # similarity command
    similarity_parser = subparsers.add_parser('similarity')
    similarity_parser.add_argument(
        'commit_hash_A',
        type = str,
        help = ''
    )
    similarity_parser.add_argument(
        'commit_hash_B',
        type = str,
        help = ''
    )
    similarity_parser.set_defaults(
        run_command = commands.similarity.run
    )

    # branch command
    branch_parser = subparsers.add_parser('branch')
    branch_parser.add_argument(
        'name',
        type = str,
        help = ''
    )
    branch_parser.set_defaults(
        run_command = commands.branch.run
    )

    # cat_object command
    cat_parser = subparsers.add_parser('cat-object')
    cat_parser.add_argument(
        'commit_hash',
        type = str,
        help = ''
    )
    cat_parser.set_defaults(
        run_command = commands.cat_object.run
    )

    status_parser = subparsers.add_parser('status')
    status_parser.set_defaults(
        run_command = commands.status.run
    )

    return parser