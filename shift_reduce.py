import re
class hebele:
    def __init__(self):
        self.stack = [0]
        self.tokens = []
        self.action_table = {0: {'id': 'S5', '+': '', '*': '', '(': 'S4', ')': '', '$': '', 'E': '1', 'T': '2', 'F': '3'},1: {'id': '', '+': 'S6', '*': '', '(': '', ')': '', '$': 'accept', 'E': '', 'T': '', 'F': ''},2: {'id': '', '+': 'R2', '*': 'S7', '(': '', ')': 'R2', '$': 'R2', 'E': '', 'T': '', 'F': ''},3: {'id': '', '+': 'R4', '*': 'R4', '(': '', ')': 'R4', '$': 'R4', 'E': '', 'T': '', 'F': ''},4: {'id': 'S5', '+': '', '*': '', '(': 'S4', ')': '', '$': '', 'E': '8', 'T': '2', 'F': '3'}, 5: {'id': '', '+': 'R6', '*': 'R6', '(': '', ')': 'R6', '$': 'R6', 'E': '', 'T': '', 'F': ''},6: {'id': 'S5', '+': '', '*': '', '(': 'S4', ')': '', '$': '', 'E': '', 'T': '9', 'F': '3'},7: {'id': 'S5', '+': '', '*': '', '(': 'S4', ')': '', '$': '', 'E': '', 'T': '', 'F': '10'},8: {'id': 'S5', '+': 'S6', '*': '', '(': '', ')': 'S11', '$': '', 'E': '', 'T': '', 'F': ''},9: {'id': '', '+': 'R1', '*': 'S7', '(': '', ')': 'R1', '$': 'R1', 'E': '', 'T': '', 'F': ''},10: {'id': '', '+': 'R3', '*': 'R3', '(': '', ')': 'R3', '$': 'R3', 'E': '', 'T': '', 'F': ''},11: {'id': '', '+': 'R5', '*': 'R5', '(': '', ')': 'R5', '$': 'R5', 'E': '', 'T': '', 'F': ''}}
        self.rules = {
            1: ['E',r'E+T',6],2: ['E',r'T',2],3: ['T',r'T*F',6],4: ['T',r'F',2],5: ['F',r'(E)',6],6: ['F',r'id',2] }
    def parse(self,user_input):
        self.stack=[0]
        self.tokens=[]
        pattern = r'(id|\+|\*|\(|\)|\$)'# Düzenli ifade tanımla
        matches = re.findall(pattern, user_input)# Düzenli ifadeye göre eşleşmeleri bul
        self.tokens.extend(matches)# Eşleşen her öğeyi tokenlar listesine ekle
        self.tokens.append('$')
        print(self.tokens)
        while self.tokens:
            i = self.tokens[0]
            action = self.action_table[self.stack[-1]][i]
            print(f"{self.stack}\t{self.tokens}\t{action}")
            if action=='accept':
                print("VALID string entered. ACCEPTED!")
                break
            elif action=='':
                print("INVALID string entered. SYNTAX ERROR!")
                break
            elif action[0]=='S':#shifting procces
                self.stack.append(i)
                self.tokens.pop(0) #token,stack'a shift olduğu için shift edileni burdan kaldırıyorum
                self.stack.append(int(action[1:]))
            elif action[0]=='R':#reducing process
                for i in range(0,self.rules[int(action[1])][2],+1):
                    self.stack.pop()
                self.stack.append(self.rules[int(action[1])][0])
                self.stack.append(int(self.action_table[self.stack[-2]][self.stack[-1]]))
if __name__ == "__main__":
    parser = hebele()
    while 1:
        user_input = input("Enter your string:\n")
        if not user_input:
            break
        parser.parse(user_input)