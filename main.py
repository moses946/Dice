import random

output = {str(i): 0 for i in range(1,7)}

def simulate_dice(rolls):
    for i in range(rolls):
        val = random.random()        
        if  0 <= val < 1/6:
            output['1'] += 1
        elif 1/6 <= val < 2/6:
            output['2'] += 1
        elif 2/6 <= val < 3/6:
            output['3'] += 1
        elif 3/6 <= val < 4/6:
            output['4'] += 1
        elif 4/6 <= val < 5/6:
            output['5'] += 1
        else:
            output['6'] += 1


if __name__ == "__main__":
    simulate_dice(1000)
    print("-"*35)
    print("| Side\t | Freq\t | Percentage\t |")
    print("-"*35)
    for key, val in output.items():
        print(f"|   {key}\t |  {val}\t |  {val/1000}\t\t |")
