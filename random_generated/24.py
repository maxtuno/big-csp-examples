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

	big_csp.Constraint(0 <= x0 <= 41)
	big_csp.Constraint(0 <= x1 <= 21)
	big_csp.Constraint(0 <= x2 <= 19)
	big_csp.Constraint(0 <= x3 <= 14)
	big_csp.Constraint(0 <= x4 <= 69)
	big_csp.Constraint(0 <= x5 <= 20)
	big_csp.Constraint(0 <= x6 <= 68)
	big_csp.Constraint(0 <= x7 <= 53)
	big_csp.Constraint(0 <= x8 <= 10)
	big_csp.Constraint(0 <= x9 <= 64)
	big_csp.Constraint(0 <= x10 <= 64)
	big_csp.Constraint(0 <= x11 <= 57)
	big_csp.Constraint(0 <= x12 <= 4)
	big_csp.Constraint(0 <= x13 <= 47)
	big_csp.Constraint(0 <= x14 <= 56)
	big_csp.Constraint(0 <= x15 <= 30)
	big_csp.Constraint(0 <= x16 <= 50)
	big_csp.Constraint(0 <= x17 <= 5)
	big_csp.Constraint(0 <= x18 <= 64)
	big_csp.Constraint(0 <= x19 <= 17)
	big_csp.Constraint(0 <= x20 <= 45)
	big_csp.Constraint(0 <= x21 <= 44)
	big_csp.Constraint(0 <= x22 <= 44)
	big_csp.Constraint(0 <= x23 <= 1)

	big_csp.Constraint(optimal < x14 + x3 * x21 ** 5 + x11 * x3 + x14 ** 2 + x7 * x6 + x10 ** 4 + x21 + x6 * 4 * x1 + x17 * x20 + 2 * x19 + x23 + x12 * x16 ** 5 + x19 + x14 * 5 * x4 + x22 + x2 * 6 * x12 + x18 + x12 * 3 * x1 + x4 * x2 + 6 * x13 + x23 + x4 * 5 * x15 + x11 * x22 + x1 ** 5)

	big_csp.Constraint(x13 * x22 + x21 ** 2 + x13 * x17 + 5 * x5 + x14 * x21 + 3 * x22 + x4 * x3 + 4 * x16 + x8 + x23 * 6 * x10 + x7 + x20 * 2 * x21 <= 204)

	big_csp.Constraint(x6 + x10 * 6 * x14 + x20 * x16 + 4 * x5 + x0 * x12 + 6 * x0 + x8 + x15 * 2 * x22 + x9 + x8 * x14 ** 6 + x10 * x21 + 3 * x7 <= 430)

	big_csp.Constraint(x19 + x13 * x12 ** 6 + x19 * x16 + 4 * x11 + x16 * x0 + x22 ** 5 + x2 * x16 + x2 ** 5 + x13 + x13 * x11 ** 5 + x4 + x1 * x13 ** 6 <= 501)

	big_csp.Constraint(x8 + x2 * x8 ** 3 + x0 + x22 * 6 * x12 + x8 + x11 * x16 ** 5 + x7 * x5 + 3 * x14 + x20 * x7 + x19 ** 2 + x17 * x3 + 6 * x8 <= 471)

	big_csp.Constraint(x12 + x5 * 4 * x0 + x6 * x16 + 3 * x20 + x13 + x18 * x10 ** 5 + x13 * x4 + 3 * x2 + x1 * x9 + 3 * x8 + x20 + x17 * 5 * x10 <= 453)

	big_csp.Constraint(x20 * x18 + x11 ** 5 + x23 + x13 * x22 ** 3 + x19 * x11 + x13 ** 5 + x17 + x11 * 4 * x15 + x14 + x21 * x4 ** 5 + x9 + x4 * x10 ** 5 <= 510)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23]):
		optimal = x14 + x3 * x21 ** 5 + x11 * x3 + x14 ** 2 + x7 * x6 + x10 ** 4 + x21 + x6 * 4 * x1 + x17 * x20 + 2 * x19 + x23 + x12 * x16 ** 5 + x19 + x14 * 5 * x4 + x22 + x2 * 6 * x12 + x18 + x12 * 3 * x1 + x4 * x2 + 6 * x13 + x23 + x4 * 5 * x15 + x11 * x22 + x1 ** 5 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23)
	else:
		break

	solver.clear()
