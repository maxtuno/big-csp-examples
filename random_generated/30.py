import big_csp

optimal = 0
while True:
	encoder = big_csp.Encoder(bits=32)

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
	x27 = big_csp.Entity(encoder)
	x28 = big_csp.Entity(encoder)
	x29 = big_csp.Entity(encoder)

	big_csp.Constraint(1 <= x0 <= 8)
	big_csp.Constraint(1 <= x1 <= 69)
	big_csp.Constraint(1 <= x2 <= 17)
	big_csp.Constraint(0 <= x3 <= 66)
	big_csp.Constraint(1 <= x4 <= 3)
	big_csp.Constraint(2 <= x5 <= 6)
	big_csp.Constraint(0 <= x6 <= 39)
	big_csp.Constraint(1 <= x7 <= 57)
	big_csp.Constraint(2 <= x8 <= 40)
	big_csp.Constraint(0 <= x9 <= 25)
	big_csp.Constraint(2 <= x10 <= 47)
	big_csp.Constraint(2 <= x11 <= 71)
	big_csp.Constraint(1 <= x12 <= 4)
	big_csp.Constraint(0 <= x13 <= 73)
	big_csp.Constraint(0 <= x14 <= 76)
	big_csp.Constraint(0 <= x15 <= 9)
	big_csp.Constraint(2 <= x16 <= 5)
	big_csp.Constraint(2 <= x17 <= 61)
	big_csp.Constraint(0 <= x18 <= 7)
	big_csp.Constraint(1 <= x19 <= 63)
	big_csp.Constraint(0 <= x20 <= 26)
	big_csp.Constraint(2 <= x21 <= 40)
	big_csp.Constraint(1 <= x22 <= 18)
	big_csp.Constraint(1 <= x23 <= 53)
	big_csp.Constraint(0 <= x24 <= 13)
	big_csp.Constraint(1 <= x25 <= 50)
	big_csp.Constraint(2 <= x26 <= 3)
	big_csp.Constraint(1 <= x27 <= 40)
	big_csp.Constraint(2 <= x28 <= 28)
	big_csp.Constraint(0 <= x29 <= 40)

	big_csp.Constraint(optimal < x25 + x28 * 4 * x9 + x20 + x21 * 4 * x9 + x2 * x17 + 5 * x28 + x26 + x22 * 6 * x10 + x28 * x20 + x9 ** 7 + x14 * x3 + x15 ** 7 + x25 + x5 * 2 * x25 + x1 + x21 * 4 * x28 + x0 * x28 + x20 ** 7 + x17 * x19 + 4 * x17 + x20 * x22 + 2 * x28 + x23 * x15 + x26 ** 4 + x5 + x27 * x23 ** 2 + x19 * x25 + x4 ** 7 + x21 * x6 + x3 ** 2)

	big_csp.Constraint(x9 * x8 + x16 ** 5 + x1 * x6 + x2 ** 6 + x4 + x13 * x1 ** 6 + x24 * x29 + 7 * x3 + x25 * x26 + x12 ** 6 + x3 + x9 * x4 ** 6 + x23 * x4 + 2 * x23 <= 829)

	big_csp.Constraint(x8 * x4 + 7 * x29 + x14 + x14 * x28 ** 2 + x13 + x8 * 7 * x15 + x8 + x14 * 3 * x14 + x7 + x20 * 4 * x0 + x1 * x27 + 2 * x17 + x12 + x2 * 5 * x20 <= 147)

	big_csp.Constraint(x5 + x14 * x5 ** 5 + x10 * x0 + 3 * x25 + x1 + x20 * x3 ** 4 + x1 + x10 * 6 * x0 + x22 + x15 * 6 * x13 + x5 + x5 * 7 * x3 + x7 + x0 * x15 ** 7 <= 88)

	big_csp.Constraint(x16 + x18 * 2 * x1 + x2 * x18 + 5 * x22 + x19 * x19 + x7 ** 2 + x26 * x28 + x11 ** 3 + x4 * x15 + x23 ** 7 + x22 * x27 + x3 ** 3 + x16 + x2 * 5 * x28 <= 812)

	big_csp.Constraint(x17 * x22 + x5 ** 4 + x27 + x5 * x27 ** 6 + x15 * x6 + x2 ** 4 + x10 + x12 * 7 * x8 + x29 * x1 + 7 * x4 + x28 + x6 * x3 ** 4 + x13 + x14 * x26 ** 7 <= 735)

	big_csp.Constraint(x11 * x28 + 3 * x14 + x27 + x1 * 7 * x1 + x26 * x11 + 6 * x24 + x19 * x24 + x20 ** 5 + x23 + x14 * 6 * x2 + x11 + x24 * x24 ** 3 + x1 * x0 + x29 ** 3 <= 789)

	big_csp.Constraint(x22 + x5 * 4 * x18 + x4 * x4 + x19 ** 4 + x2 + x25 * 5 * x7 + x0 * x12 + x8 ** 3 + x22 * x28 + x5 ** 4 + x27 * x0 + 6 * x11 + x20 * x9 + x20 ** 4 <= 461)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29]):
		optimal = x25 + x28 * 4 * x9 + x20 + x21 * 4 * x9 + x2 * x17 + 5 * x28 + x26 + x22 * 6 * x10 + x28 * x20 + x9 ** 7 + x14 * x3 + x15 ** 7 + x25 + x5 * 2 * x25 + x1 + x21 * 4 * x28 + x0 * x28 + x20 ** 7 + x17 * x19 + 4 * x17 + x20 * x22 + 2 * x28 + x23 * x15 + x26 ** 4 + x5 + x27 * x23 ** 2 + x19 * x25 + x4 ** 7 + x21 * x6 + x3 ** 2 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29)
	else:
		break

	solver.clear()
