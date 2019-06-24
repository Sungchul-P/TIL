# 각 재료와 토핑의 조합을 모두 리스트로 만들어서 반환한다.
    # 재료와 토핑 1:1 조합
# 메소드 호출 : IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops()
# 출력 결과 : [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

# 문제 원형 #
'''
class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        pass

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
'''

# 문제 풀이 #
class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        icecream_list = []
        
        # 재료와 토핑의 조합을 모두 추가
        for ingredient in self.ingredients:
            # 토핑이 한 개 이상일 때만, 추가 반복문 수행
            if len(self.toppings) > 1:
                for topping in self.toppings:
                    icecream_list.append([ingredient, topping])
            else:
                icecream_list.append([ingredient, self.toppings[0]])

        return icecream_list


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce", "strawberry sauce"])
print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]