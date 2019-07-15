import big_csp

if __name__ == '__main__':
    opt = 2 ** 8 - 1
    while True:
        encoder = big_csp.Encoder(bits=8)

        b2 = big_csp.Entity(encoder)
        b3 = big_csp.Entity(encoder)
        b4 = big_csp.Entity(encoder)
        b5 = big_csp.Entity(encoder)
        b6 = big_csp.Entity(encoder)
        b7 = big_csp.Entity(encoder)
        b8 = big_csp.Entity(encoder)
        b9 = big_csp.Entity(encoder)
        b10 = big_csp.Entity(encoder)
        b11 = big_csp.Entity(encoder)
        b12 = big_csp.Entity(encoder)
        b13 = big_csp.Entity(encoder)
        b14 = big_csp.Entity(encoder)
        b15 = big_csp.Entity(encoder)
        b16 = big_csp.Entity(encoder)
        b17 = big_csp.Entity(encoder)
        b18 = big_csp.Entity(encoder)
        b19 = big_csp.Entity(encoder)
        b20 = big_csp.Entity(encoder)
        b21 = big_csp.Entity(encoder)
        b22 = big_csp.Entity(encoder)
        b23 = big_csp.Entity(encoder)
        b24 = big_csp.Entity(encoder)
        b25 = big_csp.Entity(encoder)
        b26 = big_csp.Entity(encoder)
        b27 = big_csp.Entity(encoder)
        b28 = big_csp.Entity(encoder)
        b29 = big_csp.Entity(encoder)
        b30 = big_csp.Entity(encoder)
        b31 = big_csp.Entity(encoder)
        b32 = big_csp.Entity(encoder)
        b33 = big_csp.Entity(encoder)
        b34 = big_csp.Entity(encoder)
        b35 = big_csp.Entity(encoder)
        b36 = big_csp.Entity(encoder)
        b37 = big_csp.Entity(encoder)
        b38 = big_csp.Entity(encoder)
        b39 = big_csp.Entity(encoder)
        b40 = big_csp.Entity(encoder)
        b41 = big_csp.Entity(encoder)
        b42 = big_csp.Entity(encoder)
        b43 = big_csp.Entity(encoder)
        b44 = big_csp.Entity(encoder)
        b45 = big_csp.Entity(encoder)
        b46 = big_csp.Entity(encoder)
        b47 = big_csp.Entity(encoder)
        b48 = big_csp.Entity(encoder)
        b49 = big_csp.Entity(encoder)
        b50 = big_csp.Entity(encoder)
        b51 = big_csp.Entity(encoder)
        b52 = big_csp.Entity(encoder)
        b53 = big_csp.Entity(encoder)
        b54 = big_csp.Entity(encoder)
        b55 = big_csp.Entity(encoder)
        b56 = big_csp.Entity(encoder)
        b57 = big_csp.Entity(encoder)
        b58 = big_csp.Entity(encoder)
        b59 = big_csp.Entity(encoder)
        b60 = big_csp.Entity(encoder)
        b61 = big_csp.Entity(encoder)
        x62 = big_csp.Entity(encoder)

        big_csp.Constraint(b2 + b3 + b4 == 1)
        big_csp.Constraint(b5 + b6 + b7 == 1)
        big_csp.Constraint(b8 + b9 + b10 == 1)
        big_csp.Constraint(b11 + b12 + b13 == 1)
        big_csp.Constraint(b14 + b15 + b16 == 1)
        big_csp.Constraint(b17 + b18 + b19 == 1)
        big_csp.Constraint(b20 + b21 + b22 == 1)
        big_csp.Constraint(b23 + b24 + b25 == 1)
        big_csp.Constraint(b26 + b27 + b28 == 1)
        big_csp.Constraint(b29 + b30 + b31 == 1)
        big_csp.Constraint(b32 + b33 + b34 == 1)
        big_csp.Constraint(b35 + b36 + b37 == 1)
        big_csp.Constraint(b38 + b39 + b40 == 1)
        big_csp.Constraint(b41 + b42 + b43 == 1)
        big_csp.Constraint(b44 + b45 + b46 == 1)
        big_csp.Constraint(b47 + b48 + b49 == 1)
        big_csp.Constraint(b50 + b51 + b52 == 1)
        big_csp.Constraint(b53 + b54 + b55 == 1)
        big_csp.Constraint(b56 + b57 + b58 == 1)
        big_csp.Constraint(b59 + b60 + b61 == 1)

        variables = [b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42, b43, b44, b45, b46, b47, b48, b49, b50, b51, b52, b53, b54, b55, b56, b57, b58, b59, b60, b61]

        for b in variables:
            big_csp.Constraint(b <= 1)

        big_csp.Constraint(x62 == b59 * b56 + b60 * b57 + b61 * b58 + b56 * b53 + b57 * b54 + b58 * b55 + 2 * b59 * b53 + 2 *
                           b60 * b54 + 2 * b61 * b55 + b53 * b50 + b54 * b51 + b55 * b52 + 2 * b56 * b50 + 2 * b57 * b51
                           + 2 * b58 * b52 + 3 * b59 * b50 + 3 * b60 * b51 + 3 * b61 * b52 + b50 * b47 + b51 * b48 + b52
                           * b49 + 2 * b53 * b47 + 2 * b54 * b48 + 2 * b55 * b49 + 3 * b56 * b47 + 3 * b57 * b48 + 3 * b58 *
                           b49 + 4 * b59 * b47 + 4 * b60 * b48 + 4 * b61 * b49 + b47 * b44 + b48 * b45 + b49 * b46 + 2 *
                           b50 * b44 + 2 * b51 * b45 + 2 * b52 * b46 + 3 * b53 * b44 + 3 * b54 * b45 + 3 * b55 * b46 + 4 *
                           b56 * b44 + 4 * b57 * b45 + 4 * b58 * b46 + 5 * b59 * b44 + 5 * b60 * b45 + 5 * b61 * b46 + b44 *
                           b41 + b45 * b42 + b46 * b43 + 2 * b47 * b41 + 2 * b48 * b42 + 2 * b49 * b43 + 3 * b50 * b41 +
                           3 * b51 * b42 + 3 * b52 * b43 + 4 * b53 * b41 + 4 * b54 * b42 + 4 * b55 * b43 + 5 * b56 * b41 + 5 *
                           b57 * b42 + 5 * b58 * b43 + 6 * b59 * b41 + 6 * b60 * b42 + 6 * b61 * b43 + b41 * b38 + b42 *
                           b39 + b43 * b40 + 2 * b44 * b38 + 2 * b45 * b39 + 2 * b46 * b40 + 3 * b47 * b38 + 3 * b48 * b39
                           + 3 * b49 * b40 + 4 * b50 * b38 + 4 * b51 * b39 + 4 * b52 * b40 + 5 * b53 * b38 + 5 * b54 * b39
                           + 5 * b55 * b40 + 6 * b56 * b38 + 6 * b57 * b39 + 6 * b58 * b40 + 7 * b59 * b38 + 7 * b60 * b39
                           + 7 * b61 * b40 + b38 * b35 + b39 * b36 + b40 * b37 + 2 * b41 * b35 + 2 * b42 * b36 + 2 * b43
                           * b37 + 3 * b44 * b35 + 3 * b45 * b36 + 3 * b46 * b37 + 4 * b47 * b35 + 4 * b48 * b36 + 4 * b49 *
                           b37 + 5 * b50 * b35 + 5 * b51 * b36 + 5 * b52 * b37 + 6 * b53 * b35 + 6 * b54 * b36 + 6 * b55 *
                           b37 + 7 * b56 * b35 + 7 * b57 * b36 + 7 * b58 * b37 + 8 * b59 * b35 + 8 * b60 * b36 + 8 * b61 *
                           b37 + b35 * b32 + b36 * b33 + b37 * b34 + 2 * b38 * b32 + 2 * b39 * b33 + 2 * b40 * b34 + 3 *
                           b41 * b32 + 3 * b42 * b33 + 3 * b43 * b34 + 4 * b44 * b32 + 4 * b45 * b33 + 4 * b46 * b34 + 5 *
                           b47 * b32 + 5 * b48 * b33 + 5 * b49 * b34 + 6 * b50 * b32 + 6 * b51 * b33 + 6 * b52 * b34 + 7 *
                           b53 * b32 + 7 * b54 * b33 + 7 * b55 * b34 + 8 * b56 * b32 + 8 * b57 * b33 + 8 * b58 * b34 + 9 *
                           b59 * b32 + 9 * b60 * b33 + 9 * b61 * b34 + b32 * b29 + b33 * b30 + b34 * b31 + 2 * b35 * b29
                           + 2 * b36 * b30 + 2 * b37 * b31 + 3 * b38 * b29 + 3 * b39 * b30 + 3 * b40 * b31 + 4 * b41 * b29
                           + 4 * b42 * b30 + 4 * b43 * b31 + 5 * b44 * b29 + 5 * b45 * b30 + 5 * b46 * b31 + 6 * b47 * b29
                           + 6 * b48 * b30 + 6 * b49 * b31 + 7 * b50 * b29 + 7 * b51 * b30 + 7 * b52 * b31 + 8 * b53 * b29
                           + 8 * b54 * b30 + 8 * b55 * b31 + 9 * b56 * b29 + 9 * b57 * b30 + 9 * b58 * b31 + 10 * b59 * b29
                           + 10 * b60 * b30 + 10 * b61 * b31 + b29 * b26 + b30 * b27 + b31 * b28 + 2 * b32 * b26 + 2 *
                           b33 * b27 + 2 * b34 * b28 + 3 * b35 * b26 + 3 * b36 * b27 + 3 * b37 * b28 + 4 * b38 * b26 + 4 *
                           b39 * b27 + 4 * b40 * b28 + 5 * b41 * b26 + 5 * b42 * b27 + 5 * b43 * b28 + 6 * b44 * b26 + 6 *
                           b45 * b27 + 6 * b46 * b28 + 7 * b47 * b26 + 7 * b48 * b27 + 7 * b49 * b28 + 8 * b50 * b26 + 8 *
                           b51 * b27 + 8 * b52 * b28 + 9 * b53 * b26 + 9 * b54 * b27 + 9 * b55 * b28 + 10 * b56 * b26 + 10 *
                           b57 * b27 + 10 * b58 * b28 + 11 * b59 * b26 + 11 * b60 * b27 + 11 * b61 * b28 + b26 * b23 +
                           b27 * b24 + b28 * b25 + 2 * b29 * b23 + 2 * b30 * b24 + 2 * b31 * b25 + 3 * b32 * b23 + 3 * b33 *
                           b24 + 3 * b34 * b25 + 4 * b35 * b23 + 4 * b36 * b24 + 4 * b37 * b25 + 5 * b38 * b23 + 5 * b39 *
                           b24 + 5 * b40 * b25 + 6 * b41 * b23 + 6 * b42 * b24 + 6 * b43 * b25 + 7 * b44 * b23 + 7 * b45 *
                           b24 + 7 * b46 * b25 + 8 * b47 * b23 + 8 * b48 * b24 + 8 * b49 * b25 + 9 * b50 * b23 + 9 * b51 *
                           b24 + 9 * b52 * b25 + 10 * b53 * b23 + 10 * b54 * b24 + 10 * b55 * b25 + 11 * b56 * b23 + 11 *
                           b57 * b24 + 11 * b58 * b25 + 12 * b59 * b23 + 12 * b60 * b24 + 12 * b61 * b25 + b23 * b20 +
                           b24 * b21 + b25 * b22 + 2 * b26 * b20 + 2 * b27 * b21 + 2 * b28 * b22 + 3 * b29 * b20 + 3 * b30 *
                           b21 + 3 * b31 * b22 + 4 * b32 * b20 + 4 * b33 * b21 + 4 * b34 * b22 + 5 * b35 * b20 + 5 * b36 *
                           b21 + 5 * b37 * b22 + 6 * b38 * b20 + 6 * b39 * b21 + 6 * b40 * b22 + 7 * b41 * b20 + 7 * b42 *
                           b21 + 7 * b43 * b22 + 8 * b44 * b20 + 8 * b45 * b21 + 8 * b46 * b22 + 9 * b47 * b20 + 9 * b48 *
                           b21 + 9 * b49 * b22 + 10 * b50 * b20 + 10 * b51 * b21 + 10 * b52 * b22 + 11 * b53 * b20 + 11 *
                           b54 * b21 + 11 * b55 * b22 + 12 * b56 * b20 + 12 * b57 * b21 + 12 * b58 * b22 + 13 * b59 * b20
                           + 13 * b60 * b21 + 13 * b61 * b22 + b20 * b17 + b21 * b18 + b22 * b19 + 2 * b23 * b17 + 2 *
                           b24 * b18 + 2 * b25 * b19 + 3 * b26 * b17 + 3 * b27 * b18 + 3 * b28 * b19 + 4 * b29 * b17 + 4 *
                           b30 * b18 + 4 * b31 * b19 + 5 * b32 * b17 + 5 * b33 * b18 + 5 * b34 * b19 + 6 * b35 * b17 + 6 *
                           b36 * b18 + 6 * b37 * b19 + 7 * b38 * b17 + 7 * b39 * b18 + 7 * b40 * b19 + 8 * b41 * b17 + 8 *
                           b42 * b18 + 8 * b43 * b19 + 9 * b44 * b17 + 9 * b45 * b18 + 9 * b46 * b19 + 10 * b47 * b17 + 10 *
                           b48 * b18 + 10 * b49 * b19 + 11 * b50 * b17 + 11 * b51 * b18 + 11 * b52 * b19 + 12 * b53 * b17
                           + 12 * b54 * b18 + 12 * b55 * b19 + 13 * b56 * b17 + 13 * b57 * b18 + 13 * b58 * b19 + 14 * b59
                           * b17 + 14 * b60 * b18 + 14 * b61 * b19 + b17 * b14 + b18 * b15 + b19 * b16 + 2 * b20 * b14
                           + 2 * b21 * b15 + 2 * b22 * b16 + 3 * b23 * b14 + 3 * b24 * b15 + 3 * b25 * b16 + 4 * b26 * b14
                           + 4 * b27 * b15 + 4 * b28 * b16 + 5 * b29 * b14 + 5 * b30 * b15 + 5 * b31 * b16 + 6 * b32 * b14
                           + 6 * b33 * b15 + 6 * b34 * b16 + 7 * b35 * b14 + 7 * b36 * b15 + 7 * b37 * b16 + 8 * b38 * b14
                           + 8 * b39 * b15 + 8 * b40 * b16 + 9 * b41 * b14 + 9 * b42 * b15 + 9 * b43 * b16 + 10 * b44 * b14
                           + 10 * b45 * b15 + 10 * b46 * b16 + 11 * b47 * b14 + 11 * b48 * b15 + 11 * b49 * b16 + 12 * b50
                           * b14 + 12 * b51 * b15 + 12 * b52 * b16 + 13 * b53 * b14 + 13 * b54 * b15 + 13 * b55 * b16 + 14
                           * b56 * b14 + 14 * b57 * b15 + 14 * b58 * b16 + 15 * b59 * b14 + 15 * b60 * b15 + 15 * b61 * b16
                           + b14 * b11 + b15 * b12 + b16 * b13 + 2 * b17 * b11 + 2 * b18 * b12 + 2 * b19 * b13 + 3 * b20
                           * b11 + 3 * b21 * b12 + 3 * b22 * b13 + 4 * b23 * b11 + 4 * b24 * b12 + 4 * b25 * b13 + 5 * b26 *
                           b11 + 5 * b27 * b12 + 5 * b28 * b13 + 6 * b29 * b11 + 6 * b30 * b12 + 6 * b31 * b13 + 7 * b32 *
                           b11 + 7 * b33 * b12 + 7 * b34 * b13 + 8 * b35 * b11 + 8 * b36 * b12 + 8 * b37 * b13 + 9 * b38 *
                           b11 + 9 * b39 * b12 + 9 * b40 * b13 + 10 * b41 * b11 + 10 * b42 * b12 + 10 * b43 * b13 + 11 *
                           b44 * b11 + 11 * b45 * b12 + 11 * b46 * b13 + 12 * b47 * b11 + 12 * b48 * b12 + 12 * b49 * b13
                           + 13 * b50 * b11 + 13 * b51 * b12 + 13 * b52 * b13 + 14 * b53 * b11 + 14 * b54 * b12 + 14 * b55
                           * b13 + 15 * b56 * b11 + 15 * b57 * b12 + 15 * b58 * b13 + 16 * b59 * b11 + 16 * b60 * b12 + 16
                           * b61 * b13 + b11 * b8 + b12 * b9 + b13 * b10 + 2 * b14 * b8 + 2 * b15 * b9 + 2 * b16 * b10 + 3
                           * b17 * b8 + 3 * b18 * b9 + 3 * b19 * b10 + 4 * b20 * b8 + 4 * b21 * b9 + 4 * b22 * b10 + 5 * b23 *
                           b8 + 5 * b24 * b9 + 5 * b25 * b10 + 6 * b26 * b8 + 6 * b27 * b9 + 6 * b28 * b10 + 7 * b29 * b8 + 7
                           * b30 * b9 + 7 * b31 * b10 + 8 * b32 * b8 + 8 * b33 * b9 + 8 * b34 * b10 + 9 * b35 * b8 + 9 * b36 *
                           b9 + 9 * b37 * b10 + 10 * b38 * b8 + 10 * b39 * b9 + 10 * b40 * b10 + 11 * b41 * b8 + 11 * b42 *
                           b9 + 11 * b43 * b10 + 12 * b44 * b8 + 12 * b45 * b9 + 12 * b46 * b10 + 13 * b47 * b8 + 13 * b48 *
                           b9 + 13 * b49 * b10 + 14 * b50 * b8 + 14 * b51 * b9 + 14 * b52 * b10 + 15 * b53 * b8 + 15 * b54 *
                           b9 + 15 * b55 * b10 + 16 * b56 * b8 + 16 * b57 * b9 + 16 * b58 * b10 + 17 * b59 * b8 + 17 * b60 *
                           b9 + 17 * b61 * b10 + b8 * b5 + b9 * b6 + b10 * b7 + 2 * b11 * b5 + 2 * b12 * b6 + 2 * b13 * b7
                           + 3 * b14 * b5 + 3 * b15 * b6 + 3 * b16 * b7 + 4 * b17 * b5 + 4 * b18 * b6 + 4 * b19 * b7 + 5 * b20
                           * b5 + 5 * b21 * b6 + 5 * b22 * b7 + 6 * b23 * b5 + 6 * b24 * b6 + 6 * b25 * b7 + 7 * b26 * b5 + 7 *
                           b27 * b6 + 7 * b28 * b7 + 8 * b29 * b5 + 8 * b30 * b6 + 8 * b31 * b7 + 9 * b32 * b5 + 9 * b33 * b6
                           + 9 * b34 * b7 + 10 * b35 * b5 + 10 * b36 * b6 + 10 * b37 * b7 + 11 * b38 * b5 + 11 * b39 * b6 +
                           11 * b40 * b7 + 12 * b41 * b5 + 12 * b42 * b6 + 12 * b43 * b7 + 13 * b44 * b5 + 13 * b45 * b6 + 13
                           * b46 * b7 + 14 * b47 * b5 + 14 * b48 * b6 + 14 * b49 * b7 + 15 * b50 * b5 + 15 * b51 * b6 + 15 *
                           b52 * b7 + 16 * b53 * b5 + 16 * b54 * b6 + 16 * b55 * b7 + 17 * b56 * b5 + 17 * b57 * b6 + 17 *
                           b58 * b7 + 18 * b59 * b5 + 18 * b60 * b6 + 18 * b61 * b7 + b5 * b2 + b6 * b3 + b7 * b4 + 2 * b8 *
                           b2 + 2 * b9 * b3 + 2 * b10 * b4 + 3 * b11 * b2 + 3 * b12 * b3 + 3 * b13 * b4 + 4 * b14 * b2 + 4 *
                           b15 * b3 + 4 * b16 * b4 + 5 * b17 * b2 + 5 * b18 * b3 + 5 * b19 * b4 + 6 * b20 * b2 + 6 * b21 * b3
                           + 6 * b22 * b4 + 7 * b23 * b2 + 7 * b24 * b3 + 7 * b25 * b4 + 8 * b26 * b2 + 8 * b27 * b3 + 8 * b28
                           * b4 + 9 * b29 * b2 + 9 * b30 * b3 + 9 * b31 * b4 + 10 * b32 * b2 + 10 * b33 * b3 + 10 * b34 * b4
                           + 11 * b35 * b2 + 11 * b36 * b3 + 11 * b37 * b4 + 12 * b38 * b2 + 12 * b39 * b3 + 12 * b40 * b4
                           + 13 * b41 * b2 + 13 * b42 * b3 + 13 * b43 * b4 + 14 * b44 * b2 + 14 * b45 * b3 + 14 * b46 * b4
                           + 15 * b47 * b2 + 15 * b48 * b3 + 15 * b49 * b4 + 16 * b50 * b2 + 16 * b51 * b3 + 16 * b52 * b4
                           + 17 * b53 * b2 + 17 * b54 * b3 + 17 * b55 * b4 + 18 * b56 * b2 + 18 * b57 * b3 + 18 * b58 * b4
                           + 19 * b59 * b2 + 19 * b60 * b3 + 19 * b61 * b4)

        big_csp.Constraint(x62 < opt)

        solver = big_csp.Solver()

        if solver.satisfy(variables + [x62]):
            print('{} => {}'.format(x62, ''.join(map(str, variables))))
            opt = x62.value
            solver.clear()
        else:
            break
