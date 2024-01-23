from data import d1
import argparse

parser = argparse.ArgumentParser(description='argparse testing')
parser.add_argument('--name', '-n', type=str, default="bk", required=True, help="a programmer's name")

args = parser.parse_args()
def outer():
    print('传入的参数:', args.name)
    



