class EuclideanAlgorithm:#a class for find the GCD
    
    def gcd(self, a: int, b :int ):#Calculate the greatest common divisor of a and b
        while b != 0:#The first positive integer
           a, b = b, a % b #The second positive integer
       return a
   
    def user_input(self):
        try:
            # 获取用户输入
            a = int(input("tht first number"))
            b = int(input("the second number"))
            
            if a <= 0 or b <= 0:
                raise ValueError("Please put the interger")
            
            # 计算最大公约数
            result = self.gcd(a, b)
            print(f"{a} and {b} GCD: {result}")
        
        except ValueError as e:
            print(f"fales: {e}")

if __name__ == "__main__":
    algorithm = EuclideanAlgorithm()
    algorithm.user_input()