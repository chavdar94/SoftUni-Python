biscuits_per_worker = int(input())
number_of_workers = int(input())
competing_factory_biscuits = int(input())

biscuits_per_day = biscuits_per_worker * number_of_workers
biscuits_per_month = 0

for day in range(1, 31):
    if day % 3 == 0:
        biscuits_per_month += int(biscuits_per_day * 0.75)
    else:
        biscuits_per_month += biscuits_per_day

print(f"You have produced {biscuits_per_month} biscuits for the past month.")
percentage = abs(biscuits_per_month - competing_factory_biscuits) / competing_factory_biscuits * 100
if int(biscuits_per_month) > competing_factory_biscuits:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")
