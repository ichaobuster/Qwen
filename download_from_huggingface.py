from argparse import ArgumentParser
from huggingface_hub import snapshot_download

def _get_args():
    parser = ArgumentParser()
    parser.add_argument("-c", "--checkpoint-path", type=str, default="Qwen/Qwen-14B-Chat-Int4",
                        help="Checkpoint name or path, default to %(default)r")

    args = parser.parse_args()
    return args

def main():
    args = _get_args()
    snapshot_download(repo_id=args.checkpoint_path)

if __name__ == '__main__':
    main()
