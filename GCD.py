class EuclideanAlgorithm:#a class for find the GCD
    
    def gcd(self, a: int, b :int ):#Calculate the greatest common divisor of a and b
        while b != 0:#The first positive integer
           a, b = b, a % b #The second positive integer
       return a 