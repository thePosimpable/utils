import os, sys, hashlib, time

def removeDupes(path, uniquefiles, filePaths):	
	for file in os.listdir(path):
		filepath = f"{path}/{file}"

		if os.path.isdir(filepath) == True:
			removeDupes(filepath, uniquefiles, filePaths)

		else:
			hashed = hashFile(filepath)

			if hashed in uniquefiles:
				index_of_hashed= uniquefiles.index(hashed)
				
				os.remove(filepath)
				print(f"Removed {filepath}; matching={filePaths[index_of_hashed]}")
				print()

			else:
				uniquefiles.append(hashed)
				filePaths.append(filepath)

def hashFile(filepath):
	BLOCKSIZE = 65536
	hasher = hashlib.md5()
	
	with open(filepath, "rb") as basefile:
		buf = basefile.read(BLOCKSIZE)

		while len(buf) > 0:
			hasher.update(buf)
			buf = basefile.read(BLOCKSIZE)

	return hasher.hexdigest()

def main(basepath):
	uniquefiles = []
	filePaths = []

	if os.path.isdir(basepath) == False:
		print('No such directory. Stopping execution.')
		return

	removeDupes(basepath, uniquefiles, filePaths)
	
if __name__ == "__main__":
	start_time = time.time()

	try:
		basepath = './'
		print("BASEPATH = " + basepath)

		main(basepath)

	except IndexError:
		print('Need path argument.')

	print('Finished execution.')
	print("--- %s seconds ---" % (time.time() - start_time))