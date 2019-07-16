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

	big_csp.Constraint(0 <= x0 <= 15)
	big_csp.Constraint(0 <= x1 <= 34)
	big_csp.Constraint(0 <= x2 <= 26)
	big_csp.Constraint(0 <= x3 <= 28)
	big_csp.Constraint(0 <= x4 <= 17)
	big_csp.Constraint(0 <= x5 <= 1)
	big_csp.Constraint(0 <= x6 <= 14)
	big_csp.Constraint(0 <= x7 <= 14)
	big_csp.Constraint(0 <= x8 <= 10)
	big_csp.Constraint(0 <= x9 <= 30)
	big_csp.Constraint(0 <= x10 <= 9)
	big_csp.Constraint(0 <= x11 <= 32)
	big_csp.Constraint(0 <= x12 <= 20)
	big_csp.Constraint(0 <= x13 <= 33)
	big_csp.Constraint(0 <= x14 <= 12)
	big_csp.Constraint(0 <= x15 <= 14)
	big_csp.Constraint(0 <= x16 <= 16)
	big_csp.Constraint(0 <= x17 <= 9)
	big_csp.Constraint(0 <= x18 <= 4)
	big_csp.Constraint(0 <= x19 <= 11)
	big_csp.Constraint(0 <= x20 <= 13)
	big_csp.Constraint(0 <= x21 <= 7)
	big_csp.Constraint(0 <= x22 <= 23)
	big_csp.Constraint(0 <= x23 <= 5)
	big_csp.Constraint(0 <= x24 <= 31)
	big_csp.Constraint(0 <= x25 <= 27)
	big_csp.Constraint(0 <= x26 <= 17)
	big_csp.Constraint(0 <= x27 <= 7)
	big_csp.Constraint(0 <= x28 <= 11)

	big_csp.Constraint(optimal < x3 + x24 * x25 ** 2 + x5 + x27 * x10 ** 2 + x19 * x23 + x23 ** 3 + x19 + x26 * x1 ** 3 + x10 + x23 * x8 ** 3 + x5 + x14 * x2 ** 6 + x16 * x0 + x11 ** 6 + x8 * x16 + 6 * x14 + x22 * x27 + x12 ** 5 + x12 * x14 + 2 * x24 + x6 + x6 * x18 ** 3 + x20 + x4 * x3 ** 4 + x9 + x13 * 3 * x9 + x19 * x20 + x10 ** 2)

	big_csp.Constraint(x16 * x2 + 7 * x5 + x23 + x6 * x18 ** 3 + x22 + x19 * x9 ** 2 + x2 + x5 * x2 ** 5 + x6 + x3 * 7 * x26 + x4 * x26 + x3 ** 6 + x14 * x18 + 7 * x16 <= 169)

	big_csp.Constraint(x22 * x25 + x28 ** 7 + x22 + x0 * x22 ** 2 + x8 * x27 + 4 * x0 + x22 + x12 * 7 * x7 + x12 * x7 + 6 * x10 + x1 * x5 + 3 * x24 + x20 + x11 * 5 * x15 <= 423)

	big_csp.Constraint(x18 + x18 * 4 * x15 + x8 + x13 * x28 ** 7 + x18 + x14 * x12 ** 7 + x12 * x27 + 6 * x17 + x16 + x17 * x5 ** 6 + x17 + x26 * x6 ** 4 + x28 + x7 * x5 ** 3 <= 291)

	big_csp.Constraint(x13 + x14 * x16 ** 3 + x2 * x5 + 5 * x20 + x13 * x7 + 4 * x17 + x2 + x1 * 5 * x25 + x27 * x3 + x21 ** 7 + x10 + x11 * 7 * x9 + x16 * x20 + 7 * x22 <= 690)

	big_csp.Constraint(x26 * x8 + 2 * x4 + x8 + x10 * 5 * x3 + x11 * x19 + 5 * x1 + x3 + x8 * x23 ** 4 + x6 * x10 + x9 ** 2 + x28 * x26 + 6 * x20 + x12 + x10 * x25 ** 3 <= 712)

	big_csp.Constraint(x2 * x8 + 5 * x28 + x1 + x6 * 5 * x5 + x1 * x10 + 2 * x14 + x2 * x6 + 4 * x8 + x6 * x21 + 3 * x24 + x1 + x16 * 7 * x0 + x22 * x23 + x18 ** 3 <= 440)

	big_csp.Constraint(x14 * x27 + x18 ** 6 + x17 * x10 + x20 ** 7 + x28 + x9 * 3 * x19 + x0 * x23 + 4 * x25 + x26 + x21 * x0 ** 3 + x5 + x13 * 6 * x28 + x19 + x26 * 3 * x14 <= 732)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28]):
		optimal = x3 + x24 * x25 ** 2 + x5 + x27 * x10 ** 2 + x19 * x23 + x23 ** 3 + x19 + x26 * x1 ** 3 + x10 + x23 * x8 ** 3 + x5 + x14 * x2 ** 6 + x16 * x0 + x11 ** 6 + x8 * x16 + 6 * x14 + x22 * x27 + x12 ** 5 + x12 * x14 + 2 * x24 + x6 + x6 * x18 ** 3 + x20 + x4 * x3 ** 4 + x9 + x13 * 3 * x9 + x19 * x20 + x10 ** 2 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28)
	else:
		break

	solver.clear()
