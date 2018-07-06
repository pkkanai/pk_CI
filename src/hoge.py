class Hoge:

    def index(self):

        i = 2

        #初期値、終点、増加値
        for go in range(0,11,i):

            print(go)

            if go == 5:
                print('5いただきました！')
                return True

            if go == 10:
                print('いや5とか来ないでしょ、さすがに草')
                return False
