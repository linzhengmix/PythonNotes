
import os
import multiprocessing

def copyfile(q, source_dir, target_dir, filename):
    source_f = open(source_dir+"/"+filename,'rb')
    content = source_f.read()
    source_f.close()
    target_f = open(target_dir+"/"+filename,'wb')
    target_f.write(content)
    target_f.close()

    # 如果copy完了文件，向队列传递消息
    q.put(filename)

def main():
    source_dir = input("Please input the folder name:")
    try:
        target_dir = source_dir + "_new"
        os.mkdir(target_dir)
    except:
        pass

    file_names = os.listdir(source_dir)
    # print(file_names)

    # 创建进程池
    po = multiprocessing.Pool(5)

    # 创建队列
    q = multiprocessing.Manager().Queue()
    for file_name in file_names:
        po.apply_async(copyfile,(q,source_dir,target_dir,file_name,))

    po.close()
    # po.join()
    copy_complete = 0
    while True:
        filename = q.get()
        # print("finish copy:  %s" %filename)
        copy_complete+=1
        print("\r finish doing  %.2f %%" % (copy_complete*100 / len(file_names)))
        if copy_complete >= len(file_names):
            break


    print()




if __name__ == '__main__':
    main()