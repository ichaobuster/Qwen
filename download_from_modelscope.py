from argparse import ArgumentParser
from modelscope import snapshot_download

def _get_args():
    parser = ArgumentParser()
    parser.add_argument("-c", "--checkpoint-path", type=str, default="qwen/Qwen-14B-Chat-Int4",
                        help="Checkpoint name or path, default to %(default)r")
    parser.add_argument("-r", "--revision", type=str, default="v1.0.7",
                        help="model revision")
    # parser.add_argument("-d", "--cache-dir", type=str, default="~/.cache/modelscope/hub",
    #                     help="cache_dir for download model")

    args = parser.parse_args()
    return args

def main():
    args = _get_args()
    model_dir = snapshot_download(args.checkpoint_path, revision = args.revision)
    # model_dir = snapshot_download(args.checkpoint_path, revision = args.revision, cache_dir=args.cache_dir)

if __name__ == '__main__':
    main()
