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

	big_csp.Constraint(0 <= x0 <= 48)
	big_csp.Constraint(1 <= x1 <= 70)
	big_csp.Constraint(1 <= x2 <= 2)
	big_csp.Constraint(1 <= x3 <= 36)
	big_csp.Constraint(2 <= x4 <= 2)
	big_csp.Constraint(0 <= x5 <= 55)
	big_csp.Constraint(1 <= x6 <= 42)
	big_csp.Constraint(2 <= x7 <= 49)
	big_csp.Constraint(0 <= x8 <= 63)
	big_csp.Constraint(1 <= x9 <= 26)
	big_csp.Constraint(1 <= x10 <= 35)
	big_csp.Constraint(2 <= x11 <= 48)
	big_csp.Constraint(2 <= x12 <= 6)
	big_csp.Constraint(2 <= x13 <= 71)
	big_csp.Constraint(1 <= x14 <= 49)
	big_csp.Constraint(1 <= x15 <= 22)
	big_csp.Constraint(2 <= x16 <= 53)
	big_csp.Constraint(1 <= x17 <= 48)
	big_csp.Constraint(0 <= x18 <= 30)
	big_csp.Constraint(2 <= x19 <= 2)
	big_csp.Constraint(0 <= x20 <= 30)
	big_csp.Constraint(1 <= x21 <= 19)
	big_csp.Constraint(1 <= x22 <= 43)
	big_csp.Constraint(0 <= x23 <= 46)
	big_csp.Constraint(2 <= x24 <= 16)

	big_csp.Constraint(optimal < x23 * x13 + x14 ** 5 + x7 * x21 + 6 * x5 + x10 + x11 * 4 * x10 + x7 * x11 + x19 ** 2 + x13 * x14 + x1 ** 5 + x5 * x17 + 6 * x2 + x19 + x13 * x6 ** 2 + x3 + x4 * x1 ** 4 + x17 + x3 * x13 ** 4 + x0 * x12 + x23 ** 6 + x1 + x18 * 3 * x11 + x9 * x20 + 6 * x16)

	big_csp.Constraint(x18 + x8 * x1 ** 5 + x18 + x23 * x7 ** 4 + x0 + x5 * 5 * x21 + x22 * x23 + 4 * x17 + x4 + x19 * x4 ** 2 + x6 * x19 + x21 ** 2 <= 85)

	big_csp.Constraint(x15 * x24 + x5 ** 5 + x22 * x3 + x8 ** 4 + x16 * x24 + 5 * x3 + x17 * x9 + x14 ** 2 + x6 + x24 * x11 ** 6 + x9 * x12 + 2 * x1 <= 385)

	big_csp.Constraint(x12 + x20 * x16 ** 4 + x4 * x23 + 5 * x22 + x7 + x20 * x11 ** 4 + x11 + x19 * 4 * x13 + x4 * x2 + 3 * x17 + x9 + x21 * x5 ** 4 <= 342)

	big_csp.Constraint(x0 + x1 * x2 ** 4 + x16 + x24 * 3 * x2 + x21 * x9 + x10 ** 4 + x10 * x22 + 5 * x10 + x12 + x24 * 3 * x12 + x0 * x21 + 2 * x24 <= 541)

	big_csp.Constraint(x18 * x0 + x15 ** 6 + x6 * x17 + 6 * x7 + x12 * x18 + x16 ** 2 + x10 * x6 + 5 * x0 + x0 + x12 * x13 ** 5 + x18 + x24 * 2 * x9 <= 295)

	big_csp.Constraint(x19 + x5 * x10 ** 5 + x2 * x21 + 4 * x1 + x6 * x15 + x20 ** 4 + x12 + x16 * x7 ** 4 + x9 + x24 * x6 ** 6 + x13 + x14 * 5 * x10 <= 69)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24]):
		optimal = x23 * x13 + x14 ** 5 + x7 * x21 + 6 * x5 + x10 + x11 * 4 * x10 + x7 * x11 + x19 ** 2 + x13 * x14 + x1 ** 5 + x5 * x17 + 6 * x2 + x19 + x13 * x6 ** 2 + x3 + x4 * x1 ** 4 + x17 + x3 * x13 ** 4 + x0 * x12 + x23 ** 6 + x1 + x18 * 3 * x11 + x9 * x20 + 6 * x16 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24)
	else:
		break

	solver.clear()
