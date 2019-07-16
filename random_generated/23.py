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

	big_csp.Constraint(0 <= x0 <= 30)
	big_csp.Constraint(1 <= x1 <= 40)
	big_csp.Constraint(6 <= x2 <= 71)
	big_csp.Constraint(5 <= x3 <= 20)
	big_csp.Constraint(2 <= x4 <= 27)
	big_csp.Constraint(3 <= x5 <= 11)
	big_csp.Constraint(1 <= x6 <= 56)
	big_csp.Constraint(1 <= x7 <= 36)
	big_csp.Constraint(6 <= x8 <= 37)
	big_csp.Constraint(5 <= x9 <= 13)
	big_csp.Constraint(3 <= x10 <= 49)
	big_csp.Constraint(6 <= x11 <= 35)
	big_csp.Constraint(0 <= x12 <= 55)
	big_csp.Constraint(2 <= x13 <= 74)
	big_csp.Constraint(6 <= x14 <= 22)
	big_csp.Constraint(3 <= x15 <= 6)
	big_csp.Constraint(5 <= x16 <= 18)
	big_csp.Constraint(5 <= x17 <= 18)
	big_csp.Constraint(6 <= x18 <= 38)
	big_csp.Constraint(5 <= x19 <= 56)
	big_csp.Constraint(0 <= x20 <= 34)
	big_csp.Constraint(2 <= x21 <= 13)
	big_csp.Constraint(5 <= x22 <= 41)

	big_csp.Constraint(optimal < x0 * x19 + x20 ** 4 + x1 + x5 * x3 ** 2 + x10 + x0 * 3 * x20 + x15 + x1 * 2 * x22 + x13 * x12 + 3 * x19 + x19 + x9 * 3 * x6 + x8 + x19 * 5 * x13 + x21 * x6 + 4 * x17 + x21 + x8 * x2 ** 3 + x20 + x8 * 4 * x19 + x16 * x12 + 2 * x13)

	big_csp.Constraint(x21 + x10 * x17 ** 3 + x19 * x7 + x14 ** 4 + x18 * x6 + x3 ** 3 + x5 * x4 + 5 * x18 + x12 * x1 + x10 ** 5 <= 321)

	big_csp.Constraint(x18 * x2 + x13 ** 4 + x12 * x8 + 4 * x9 + x4 + x21 * 3 * x0 + x10 + x0 * x17 ** 2 + x11 * x6 + 4 * x22 <= 72)

	big_csp.Constraint(x19 + x10 * x19 ** 5 + x7 * x1 + x18 ** 2 + x11 * x11 + 2 * x21 + x5 * x5 + 3 * x2 + x1 + x18 * 4 * x8 <= 64)

	big_csp.Constraint(x1 * x19 + x6 ** 4 + x16 * x2 + 5 * x16 + x15 + x22 * 4 * x19 + x16 * x10 + x10 ** 5 + x9 * x16 + x18 ** 5 <= 271)

	big_csp.Constraint(x22 * x22 + x8 ** 2 + x21 * x1 + x5 ** 2 + x20 + x13 * x1 ** 4 + x15 + x16 * 3 * x3 + x15 * x1 + x12 ** 5 <= 149)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22]):
		optimal = x0 * x19 + x20 ** 4 + x1 + x5 * x3 ** 2 + x10 + x0 * 3 * x20 + x15 + x1 * 2 * x22 + x13 * x12 + 3 * x19 + x19 + x9 * 3 * x6 + x8 + x19 * 5 * x13 + x21 * x6 + 4 * x17 + x21 + x8 * x2 ** 3 + x20 + x8 * 4 * x19 + x16 * x12 + 2 * x13 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22)
	else:
		break

	solver.clear()
