from pymongo import MongoClient
import gridfs


# 获取数据库对象
conn = MongoClient('localhost',27017)
db = conn.grid

# 获取文件集合对象
fs = gridfs.GridFS(db)
# 获取文件集
files = fs.find()
for file in files:
    print(file.filename)
    if file.filename == './03-常见的OS.mp4':
        with open(file.filename,'wb') as f:
            data = file.read()
            # 写入本地
            f.write(data)
conn.close()