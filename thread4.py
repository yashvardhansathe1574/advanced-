from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == "__main__":
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 56, 5, 47, 4, 85]
    
    with Pool(20) as pool:
        results = pool.map(square, numbers)
        
    print(results)
