class Computer:
    def __init__(
        self,
        brand:str,
        capacity:int,
        ram:int
    ):
        self.brand = brand
        self.capacity = capacity
        self.ram = ram
    
    def __str__(self):
        return f"{self.brand}/{self.capacity}GB/{self.ram}GB"
    
    def __del__(self):
        print(f"eliminamos a {self}")
        
if __name__ == "__main__":
    pc = Computer("HP",520,8)
    print(pc)