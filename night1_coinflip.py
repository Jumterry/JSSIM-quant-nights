import random

pnl = 0
num_flips = 1000

for i in range(num_flips):
    if random.random() < 0.5: # 50% chance of heads
        pnl += 1 # win $1
    else:
        pnl -= 1 # lose $1

print(f"Final PnL after {num_flips} flips: ${pnl}")
print(f"EV per flip: ${pnl/num_flips:.4f}")
