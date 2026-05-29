import random

bankroll = 100.0
spread = 0.10
kelly_f = 0.0455  # 4.55% Kelly fraction
num_flips = 1000

print(f"Starting bankroll: ${bankroll}")
print(f"Kelly fraction: {kelly_f*100:.2f}%\n")

for i in range(num_flips):
    bet_size = bankroll * kelly_f
    if random.random() < 0.5:
        bankroll += bet_size * (1 + spread)  # win $1.10 per $1 bet
    else:
        bankroll += bet_size * (-1 + spread) # lose $0.90 per $1 bet
    
    if i % 200 == 0:
        print(f"Flip {i}: Bankroll ${bankroll:.2f}")

print(f"\nFinal bankroll after {num_flips} flips: ${bankroll:.2f}")
print(f"Total return: {(bankroll/100 - 1)*100:.1f}%")
