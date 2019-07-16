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

	big_csp.Constraint(3 <= x0 <= 25)
	big_csp.Constraint(2 <= x1 <= 8)
	big_csp.Constraint(5 <= x2 <= 27)
	big_csp.Constraint(4 <= x3 <= 29)
	big_csp.Constraint(4 <= x4 <= 19)
	big_csp.Constraint(5 <= x5 <= 35)
	big_csp.Constraint(6 <= x6 <= 35)
	big_csp.Constraint(4 <= x7 <= 27)
	big_csp.Constraint(1 <= x8 <= 18)
	big_csp.Constraint(1 <= x9 <= 50)
	big_csp.Constraint(5 <= x10 <= 10)
	big_csp.Constraint(6 <= x11 <= 12)
	big_csp.Constraint(2 <= x12 <= 16)
	big_csp.Constraint(3 <= x13 <= 31)
	big_csp.Constraint(4 <= x14 <= 17)
	big_csp.Constraint(1 <= x15 <= 39)
	big_csp.Constraint(6 <= x16 <= 16)
	big_csp.Constraint(0 <= x17 <= 54)
	big_csp.Constraint(1 <= x18 <= 17)
	big_csp.Constraint(1 <= x19 <= 39)
	big_csp.Constraint(0 <= x20 <= 10)
	big_csp.Constraint(4 <= x21 <= 58)
	big_csp.Constraint(4 <= x22 <= 37)
	big_csp.Constraint(2 <= x23 <= 23)
	big_csp.Constraint(4 <= x24 <= 41)
	big_csp.Constraint(4 <= x25 <= 25)

	big_csp.Constraint(optimal < x24 + x4 * x7 ** 2 + x15 * x5 + x9 ** 4 + x11 * x10 + x23 ** 6 + x0 * x18 + 6 * x25 + x25 * x22 + x25 ** 3 + x15 * x3 + 4 * x12 + x0 + x18 * x2 ** 4 + x9 + x18 * 4 * x12 + x15 + x13 * 2 * x8 + x3 + x16 * 4 * x18 + x4 * x10 + 5 * x13 + x12 * x4 + x22 ** 4 + x5 + x6 * x2 ** 4)

	big_csp.Constraint(x23 + x21 * 2 * x5 + x25 * x23 + x19 ** 6 + x1 + x15 * 5 * x2 + x0 + x8 * 6 * x12 + x11 + x18 * 5 * x3 + x15 * x24 + 4 * x18 <= 555)

	big_csp.Constraint(x22 * x23 + 2 * x10 + x1 * x21 + 2 * x15 + x13 + x19 * x6 ** 3 + x16 + x16 * 6 * x16 + x5 + x16 * x15 ** 5 + x9 + x14 * x12 ** 2 <= 502)

	big_csp.Constraint(x7 * x11 + 3 * x7 + x19 * x3 + 4 * x17 + x12 + x13 * 5 * x9 + x18 + x6 * 3 * x12 + x6 + x4 * x23 ** 3 + x4 + x21 * x16 ** 3 <= 86)

	big_csp.Constraint(x15 + x16 * 3 * x7 + x25 * x14 + 3 * x0 + x18 + x4 * x3 ** 4 + x4 + x20 * x14 ** 5 + x6 * x3 + x21 ** 5 + x25 * x13 + x5 ** 4 <= 159)

	big_csp.Constraint(x5 * x5 + x19 ** 5 + x12 + x23 * x19 ** 6 + x12 * x18 + 6 * x2 + x22 * x12 + x13 ** 2 + x2 + x18 * x20 ** 4 + x3 * x17 + x19 ** 5 <= 101)

	big_csp.Constraint(x5 * x12 + 3 * x14 + x21 + x0 * 5 * x7 + x3 * x5 + 2 * x9 + x4 + x4 * 3 * x1 + x1 + x12 * x12 ** 6 + x9 * x1 + x19 ** 3 <= 480)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25]):
		optimal = x24 + x4 * x7 ** 2 + x15 * x5 + x9 ** 4 + x11 * x10 + x23 ** 6 + x0 * x18 + 6 * x25 + x25 * x22 + x25 ** 3 + x15 * x3 + 4 * x12 + x0 + x18 * x2 ** 4 + x9 + x18 * 4 * x12 + x15 + x13 * 2 * x8 + x3 + x16 * 4 * x18 + x4 * x10 + 5 * x13 + x12 * x4 + x22 ** 4 + x5 + x6 * x2 ** 4 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25)
	else:
		break

	solver.clear()
