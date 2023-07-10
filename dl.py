import requests
import sys
import os

def create_dir(manga_title):
	folder_path = f'{manga_title}'

	if not os.path.exists(folder_path):
		os.makedirs(folder_path)
		print(f"create {folder_path}")

	return folder_path

def dl_file(image_base_url, file_url):
	dl_success = True
	http_complete_url = f"{image_base_url}/{file_url}"

	print(f"downloading {http_complete_url}...", end = " ")
	response = requests.get(http_complete_url, stream=True)

	if not response.ok:
		print(response)
		dl_success = False

	print(f"dl_success = {not not response}")

	return response

def save_file(folder_path, file_url, response):
	local_file_url = f'{folder_path}/{file_url}'
	print(f"saving {local_file_url}...", end = " ")

	with open(local_file_url, 'wb') as handle:		
		for block in response.iter_content(1024):
			if not block:
				break

			handle.write(block)

	print("success")

def main(manga_title, image_base_url, filename_pattern):
	folder_path = create_dir(manga_title)
	counter = 1

	done = False

	while not done:
		filename = f"{filename_pattern % (counter,)}" if filename_pattern else f"{'%03d' % (counter,)}"
		jpg_url = f"{filename}.jpg"
		png_url = f"{filename}.png"

		file_url = jpg_url

		response = dl_file(image_base_url, jpg_url)
		if not response:
			response = dl_file(image_base_url, png_url)
			file_url = png_url

		if not response:
			done = True

		if done == False:
			save_file(folder_path, file_url, response)
			counter += 1

	
if __name__ == "__main__":
	# python dl.py "title" "imageurl" "OPTIONAL %%03d_1"

	manga_title = sys.argv[1]
	image_base_url = sys.argv[2]

	try:
		filename_pattern = sys.argv[3]

	except:
		filename_pattern = None

	main(manga_title, image_base_url, filename_pattern)