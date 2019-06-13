"""
递归：
让方案更清晰，没有性能上的优势
"""

class find_the_key(object):

    def look_for_key_normal(self,main_box):
        pile = main_box.make_a_pile_to_look_through()
        while pile is not empty:
            box = pile.grab_a_box():
            for item in box:
                if item.is_a_box():
                    pile.append(item)
                elif item.is_a_key():
                    print("found the key!")

    def look_for_key_recursive(self,box):#使用递归
        for item in box:
            if item.is_a_box():
                self.look_for_key_recursive(item)
            elif item.is_a_key():
                print('found the key!')


#基线条件与递归条件
def countdown(i):
    print(i)
    if i <= 0:  #基线条件
        return
    else:   #递归条件
        countdown(i-1)


#栈：后进先出
class stack_test(object):

    def greet(self,name):
        print("hello,"+name+"!")
        self.greet2(name)
        print("getting ready to say bye...")
        self.bye()

    def greet2(self,name):
        print("how are you,"+name+"?")

    def bye(self):
        print('ok,bye!')

test = stack_test()
test.greet('hwh')


#递归调用栈
def fact(x):
    if x == 1:
        return x
    else:
        return x*fact(x-1)

