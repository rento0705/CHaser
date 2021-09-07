import CHaser
import random
import time

def main():
    print("U-16プロコンのためのCHaserシステム")
    print("開発者ネットワークに接続しています")
    print("情報照会中")
    time.sleep(5)
    print("情報照会完了")
    print("開発者名:Rento_0705")
    print("バージョン:β20.0")
    print("更新はありません。操作を続行します。")
    print("ポート番号を2010、ユーザー名はRento0705、アドレスを127.0.0.1に指定してください。")
    value = []
    client = CHaser.Client()

    turn = 1

    while(True):
        number1 = random.randint(1, 3)
        if (turn % 3) == 1:
            #検索開始
            print("検索を開始します。")
            value = client.get_ready()
            print("Get_Ready操作を行いました")
            value = client.search_up()
            print("Search_UPを行いました。")
            value = client.get_ready()
            print("Get_Ready操作を行いました")
            value = client.search_down()
            print("Search_Downを行いました。")
            value = client.get_ready()
            print("Get_Ready操作を行いました")
            value = client.search_left()
            print("Search_Leftを行いました。")
            value = client.get_ready()
            print("Get_Ready操作を行いました")
            value = client.search_right()
            print("Search_rightを行いました。")
            #探索終了
            turn += 1
        else:
            print("ランダム移動を開始します。")
            number = random.randint(0, 3)
            value = client.get_ready()
            print("Get_Ready操作を行いました")
            if value[1]==0:
                client.walk_up()
                print("Walk_UPを行いました。")
            elif value[7]==0:
                client.walk_down()
                print("Walk_Downを行いました。")
            elif value[5]==0:
                client.walk_right()
                print("Walk_Rightを行いました。")
            elif value[3]==0:
                client.walk_left()
                print("Walk_Leftを行いました。")
            else:
                if number == 0:
                    client.walk_up()
                    print("Walk_UPを行いました。")
                elif number == 1:
                    client.walk_down()
                    print("Walk_Dowmを行いました。")
                elif number == 2:
                    client.walk_left()
                    print("Walk_Leftを行いました。")
                elif number == 3:
                    client.walk_right()
                    print("Walk_Rightを行いました。")
            turn += 1

        if number1==2:
            #アイテム式開始
            print("アイテムがあればアイテムの方へ移動します。なかった場合、ランダム移動を行います。")
            value = client.get_ready()
            print("Get_Ready操作を行いました")
            value = client.search_up()
            print("Search_UPを行いました。")
            value = client.get_ready()
            print("Get_Ready操作を行いました")
            value = client.search_down()
            print("Search_Downを行いました。")
            value = client.get_ready()
            print("Get_Ready操作を行いました")
            value = client.search_left()
            print("Search_Leftを行いました。")
            value = client.get_ready()
            print("Get_Ready操作を行いました")
            value = client.search_right()
            print("Search_Rightを行いました。")
            value = client.get_ready()
            print("Get_Ready操作を行いました")
            print(value)
            if value[1]==1:
                client.walk_up()
                print("Walk_UPを行いました。")
            elif value[7]==3:
                client.walk_down()
                print("Walk_Downを行いました。")
            elif value[5]==3:
                client.walk_right()
                print("Walk_Rightを行いました。")
            elif value[3]==3:
                client.walk_left()
                print("Walk_Leftを行いました。")
            else:
                print("アイテムが見つかりませんでした。")
                if value[1]==0:
                    client.walk_up()
                    print("Walk_UPを行いました。")
                elif value[7]==0:
                    client.walk_down()
                    print("Walk_Downを行いました。")
                elif value[5]==0:
                    client.walk_right()
                    print("Walk_Rightを行いました。")
                elif value[3]==0:
                    client.walk_left()
                    print("Walk_Leftを行いました。")
                else:
                    number = random.randint(0, 3)
                    print("アイテムが見つからなかったため、ランダム移動を開始します。")
                    if number == 0:
                        client.walk_up()
                        print("Walk_UPを行いました。")
                    elif number == 1:
                        client.walk_down()
                        print("Walk_Downを行いました。")
                    elif number == 2:
                        client.walk_left()
                        print("Walk_Leftを行いました。")
                    elif number == 3:
                        client.walk_right()
                        print("Walk_Rightを行いました。")
            turn += 1

        if number1==3:
            #敵サーチ開始
            print("敵のサーチを行います。敵がいればブロックを設置しますが、いなければsearchを行います。")
            client.get_ready()
            print("Get_Ready操作を行いました")
            print(value)
            if value[1]==1:
                value = client.put_up()
                print("Put_Upを行いました。")
            elif value[7]==1:
                value = client.put_down()
                print("Put_Downを行いました。")
            elif value[5]==1:
                value = client.put_right()
                print("Put_Rightを行いました。")
            elif value[3]==1:
                value = client.put_left()
                print("Put_Leftを行いました。")
            else:
                    print("敵が見つからないため、サーチを行います。")
                    value = client.look_up()
                    print("Look_Up操作を行いました。")
                    client.get_ready()
                    print("Get_Ready操作を行いました")
                    value = client.look_down()
                    print("Look_Down操作を行いました。")
                    client.get_ready()
                    print("Get_Ready操作を行いました")
                    value = client.look_left()
                    print("Look_Left操作を行いました。")
                    client.get_ready()
                    print("Get_Ready操作を行いました")
                    value = client.look_right()
                    print("Look_Right操作を行いました。")
        
        if 

            #敵サーチ終了
            turn += 1



        print("現在のターン数:{0}".format(turn))


#Stop Program


if __name__ == "__main__":
    main()