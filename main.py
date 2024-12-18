from snake import SnackEnv
from train import train
from test import test 


def main():
    print("*************************************")
    n = int(input("Nhập và kích thước khung hình : "))
    env = SnackEnv(n)
    
    while True:
        print("Lựa chọn : ")
        print("1. Train")
        print("2. Test ")
        print("3. Thoat ")
        i = int(input("Nhap lua chon cua ban(1 hoac 2): "))
        print("*************************************")
        if i == 1:
            train(env, episodes=30000)
            print("*************************************")
        elif i==2:
            test(env,2*n)
            print("*************************************")
        else:
            print("*************************************")
            break
    print("Hoàn thành chương trình!!!")

if __name__ == '__main__':
    main()