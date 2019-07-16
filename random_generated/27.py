import big_csp

optimal = 0
while True:
	encoder = big_csp.Encoder(bits=16)

	x0 = big_csp.Entity(encoder)
	x1 = big_csp.Entity(encoder)
	x2 = big_csp.Entity(encoder)
	x3 = big_csp.Entity(encoder)
	x4 = big_csp.Entity(encoder)
	x5 = big_csp.Entity(encoder)
	x6 = big_csp.Entity(encoder)
	x7 = big_csp.Entity(encoder)
	x8 = big_csp.Entity(encoder)
	x9 = big_csp.Entity(encoder)
	x10 = big_csp.Entity(encoder)
	x11 = big_csp.Entity(encoder)
	x12 = big_csp.Entity(encoder)
	x13 = big_csp.Entity(encoder)
	x14 = big_csp.Entity(encoder)
	x15 = big_csp.Entity(encoder)
	x16 = big_csp.Entity(encoder)
	x17 = big_csp.Entity(encoder)
	x18 = big_csp.Entity(encoder)
	x19 = big_csp.Entity(encoder)
	x20 = big_csp.Entity(encoder)
	x21 = big_csp.Entity(encoder)
	x22 = big_csp.Entity(encoder)
	x23 = big_csp.Entity(encoder)
	x24 = big_csp.Entity(encoder)
	x25 = big_csp.Entity(encoder)
	x26 = big_csp.Entity(encoder)

	big_csp.Constraint(1 <= x0 <= 15)
	big_csp.Constraint(3 <= x1 <= 20)
	big_csp.Constraint(8 <= x2 <= 17)
	big_csp.Constraint(0 <= x3 <= 16)
	big_csp.Constraint(7 <= x4 <= 10)
	big_csp.Constraint(1 <= x5 <= 19)
	big_csp.Constraint(8 <= x6 <= 12)
	big_csp.Constraint(3 <= x7 <= 17)
	big_csp.Constraint(10 <= x8 <= 20)
	big_csp.Constraint(3 <= x9 <= 12)
	big_csp.Constraint(2 <= x10 <= 14)
	big_csp.Constraint(4 <= x11 <= 16)
	big_csp.Constraint(5 <= x12 <= 22)
	big_csp.Constraint(6 <= x13 <= 18)
	big_csp.Constraint(2 <= x14 <= 20)
	big_csp.Constraint(2 <= x15 <= 18)
	big_csp.Constraint(1 <= x16 <= 19)
	big_csp.Constraint(6 <= x17 <= 19)
	big_csp.Constraint(3 <= x18 <= 16)
	big_csp.Constraint(2 <= x19 <= 21)
	big_csp.Constraint(1 <= x20 <= 14)
	big_csp.Constraint(0 <= x21 <= 18)
	big_csp.Constraint(7 <= x22 <= 18)
	big_csp.Constraint(5 <= x23 <= 21)
	big_csp.Constraint(9 <= x24 <= 10)
	big_csp.Constraint(6 <= x25 <= 15)
	big_csp.Constraint(7 <= x26 <= 10)

	big_csp.Constraint(optimal < x23 * x0 + x8 ** 3 + x24 * x7 + 3 * x4 + x15 * x17 + x0 ** 2 + x26 + x11 * x1 ** 6 + x23 * x19 + x15 ** 3 + x7 * x19 + 2 * x16 + x11 * x26 + 3 * x18 + x22 * x18 + 5 * x20 + x4 + x5 * 4 * x26 + x25 + x12 * x17 ** 6 + x8 * x21 + 4 * x20 + x1 * x7 + 6 * x8 + x9 * x24 + x0 ** 6)

	big_csp.Constraint(x6 * x19 + 4 * x3 + x15 * x24 + 6 * x14 + x26 + x18 * 6 * x14 + x24 + x6 * 3 * x17 + x26 + x17 * x16 ** 3 + x24 + x0 * 4 * x17 <= 300)

	big_csp.Constraint(x12 * x8 + 5 * x22 + x1 + x14 * 5 * x6 + x10 + x16 * x24 ** 3 + x20 + x20 * x1 ** 2 + x10 * x20 + x10 ** 4 + x9 + x17 * 6 * x7 <= 568)

	big_csp.Constraint(x21 * x21 + x8 ** 2 + x18 + x22 * 3 * x1 + x17 + x14 * x18 ** 6 + x4 + x3 * 6 * x25 + x2 + x13 * x20 ** 4 + x26 * x20 + 6 * x26 <= 314)

	big_csp.Constraint(x9 * x3 + x11 ** 3 + x22 + x10 * 5 * x2 + x1 + x20 * x18 ** 6 + x24 + x21 * 4 * x18 + x14 + x3 * x26 ** 3 + x4 + x9 * 4 * x17 <= 293)

	big_csp.Constraint(x2 + x26 * x18 ** 4 + x21 + x25 * x25 ** 3 + x4 * x8 + x21 ** 6 + x6 + x4 * x13 ** 4 + x21 + x19 * 6 * x16 + x23 * x22 + 2 * x6 <= 304)

	big_csp.Constraint(x25 + x24 * x0 ** 3 + x12 + x9 * 2 * x15 + x2 * x3 + 3 * x22 + x26 * x13 + x17 ** 4 + x5 + x6 * x3 ** 2 + x22 * x7 + 4 * x20 <= 355)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26]):
		optimal = x23 * x0 + x8 ** 3 + x24 * x7 + 3 * x4 + x15 * x17 + x0 ** 2 + x26 + x11 * x1 ** 6 + x23 * x19 + x15 ** 3 + x7 * x19 + 2 * x16 + x11 * x26 + 3 * x18 + x22 * x18 + 5 * x20 + x4 + x5 * 4 * x26 + x25 + x12 * x17 ** 6 + x8 * x21 + 4 * x20 + x1 * x7 + 6 * x8 + x9 * x24 + x0 ** 6 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26)
	else:
		break

	solver.clear()
