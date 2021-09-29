from utils import *

if __name__ == "__main__":
	print("What do you want: ")
	key = input()
	path = key + "imgs"
	print("Number of images?")
	max_n = int(input())

	download_in_parallel(path, key, max_n)
	remove_bad_images(path)