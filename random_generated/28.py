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

	big_csp.Constraint(2 <= x0 <= 7)
	big_csp.Constraint(1 <= x1 <= 16)
	big_csp.Constraint(1 <= x2 <= 62)
	big_csp.Constraint(1 <= x3 <= 50)
	big_csp.Constraint(2 <= x4 <= 62)
	big_csp.Constraint(2 <= x5 <= 84)
	big_csp.Constraint(2 <= x6 <= 55)
	big_csp.Constraint(2 <= x7 <= 74)
	big_csp.Constraint(0 <= x8 <= 90)
	big_csp.Constraint(0 <= x9 <= 15)
	big_csp.Constraint(0 <= x10 <= 45)
	big_csp.Constraint(1 <= x11 <= 6)
	big_csp.Constraint(2 <= x12 <= 30)
	big_csp.Constraint(1 <= x13 <= 11)
	big_csp.Constraint(0 <= x14 <= 51)
	big_csp.Constraint(2 <= x15 <= 72)
	big_csp.Constraint(0 <= x16 <= 63)
	big_csp.Constraint(1 <= x17 <= 72)
	big_csp.Constraint(1 <= x18 <= 83)
	big_csp.Constraint(0 <= x19 <= 86)
	big_csp.Constraint(1 <= x20 <= 30)
	big_csp.Constraint(2 <= x21 <= 85)
	big_csp.Constraint(2 <= x22 <= 90)
	big_csp.Constraint(0 <= x23 <= 70)
	big_csp.Constraint(1 <= x24 <= 35)
	big_csp.Constraint(1 <= x25 <= 21)
	big_csp.Constraint(1 <= x26 <= 36)
	big_csp.Constraint(1 <= x27 <= 4)

	big_csp.Constraint(optimal < x20 + x4 * 6 * x4 + x22 * x11 + 6 * x1 + x17 + x25 * 2 * x0 + x0 + x25 * 2 * x13 + x14 * x19 + x5 ** 3 + x16 + x16 * x19 ** 6 + x5 * x19 + 4 * x1 + x6 * x5 + 4 * x24 + x7 * x9 + x27 ** 3 + x22 + x23 * 2 * x18 + x20 + x24 * 2 * x5 + x3 * x13 + x2 ** 6 + x8 + x4 * 5 * x21 + x9 + x12 * 3 * x1)

	big_csp.Constraint(x8 * x26 + 3 * x12 + x5 * x8 + x16 ** 5 + x20 + x10 * 3 * x5 + x11 * x7 + 2 * x15 + x22 * x25 + 7 * x23 + x12 * x22 + 7 * x20 + x6 + x13 * x23 ** 7 <= 722)

	big_csp.Constraint(x13 * x0 + x24 ** 5 + x1 * x27 + x8 ** 2 + x17 * x7 + 4 * x7 + x18 + x2 * x2 ** 5 + x18 + x8 * x25 ** 2 + x20 + x14 * 4 * x2 + x9 + x24 * x2 ** 7 <= 392)

	big_csp.Constraint(x10 * x15 + x22 ** 2 + x0 * x3 + 3 * x22 + x13 + x19 * x19 ** 2 + x10 + x7 * x7 ** 6 + x1 * x16 + 7 * x10 + x14 * x8 + x27 ** 7 + x1 * x4 + 3 * x9 <= 655)

	big_csp.Constraint(x12 + x24 * 2 * x2 + x9 + x19 * x11 ** 7 + x16 + x17 * 2 * x10 + x6 + x19 * 3 * x3 + x16 + x1 * x17 ** 5 + x2 + x25 * 3 * x24 + x10 * x26 + 7 * x11 <= 630)

	big_csp.Constraint(x5 * x27 + x16 ** 6 + x15 + x25 * x2 ** 6 + x20 + x0 * x10 ** 3 + x14 + x14 * 3 * x3 + x22 + x21 * 3 * x10 + x17 + x14 * x1 ** 4 + x11 * x24 + x1 ** 6 <= 245)

	big_csp.Constraint(x1 + x13 * x26 ** 5 + x18 + x27 * 4 * x7 + x1 * x7 + x14 ** 5 + x3 * x13 + 6 * x15 + x1 * x27 + 5 * x6 + x3 * x2 + x24 ** 2 + x17 + x9 * x18 ** 6 <= 764)

	big_csp.Constraint(x18 * x27 + 7 * x2 + x9 + x9 * 7 * x10 + x15 + x17 * 7 * x17 + x17 * x9 + x23 ** 7 + x17 + x24 * x10 ** 4 + x11 * x16 + 5 * x2 + x7 + x27 * 6 * x19 <= 581)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27]):
		optimal = x20 + x4 * 6 * x4 + x22 * x11 + 6 * x1 + x17 + x25 * 2 * x0 + x0 + x25 * 2 * x13 + x14 * x19 + x5 ** 3 + x16 + x16 * x19 ** 6 + x5 * x19 + 4 * x1 + x6 * x5 + 4 * x24 + x7 * x9 + x27 ** 3 + x22 + x23 * 2 * x18 + x20 + x24 * 2 * x5 + x3 * x13 + x2 ** 6 + x8 + x4 * 5 * x21 + x9 + x12 * 3 * x1 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27)
	else:
		break

	solver.clear()
