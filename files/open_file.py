import os

if os.path.exists("file-dir/test/demo-file.txt"):
  f = open("file-dir/test/demo-file.txt", "rt")
  print(f.read())
  f.close()
else:
  print("demo-file.txt is not exist to read.")

with open("file-dir/test/demo-file.txt", "a") as f:
  f.write(" This is new line.")

with open("file-dir/test/demo-file.txt") as f:
  print(f.readline())

if os.path.exists("demo-file.txt"):
  os.remove("demo-file.txt")
else:
  print("demo-file.txt is not exist to remove.")

os.rmdir("test")
