import os,stat

for root, dirs, files in os.walk(r'C:\ness'):
    for fname in files:
        full_path = os.path.join(root, fname)
        os.chmod(full_path ,stat.S_IWRITE)
        print(full_path,"succesful")
