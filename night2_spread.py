import random

spread = 0.10
pnl = 0
num_flips = 1000

for i in range(num_flips):
    if random.random() < 0.5:
        pnl += 1 + spread # win AND collect spread
    else:
        pnl += -1 + spread # lose, but spread cushions it

print(f"Final PnL after {num_flips} flips: ${pnl:.2f}")
print(f"EV per flip: ${pnl/num_flips:.4f}")
