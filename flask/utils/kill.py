import os
import argparse
import time
parser = argparse.ArgumentParser(description="")
parser.add_argument('-p', '--path', default='')
args = parser.parse_args()
time.sleep(300)
os.system('rm %s'%args.path)