import math

def gauss(matrix, vecb, vecx, g):
    """
    Gaussian elimination with partial pivoting.
    Modifies matrix and vecb in place, stores solution in vecx.
    """
    s = [0] * (g - 1)  # pivot row indices

    # LU factorization
    for k in range(g - 1):
        # Pivot search
        z = 0.0
        sk = k
        for i in range(k, g):
            hilf = abs(matrix[i][k])
            if hilf > z:
                z = hilf
                sk = i
        s[k] = sk

        # Swap rows if needed
        if sk > k:
            matrix[k], matrix[sk] = matrix[sk], matrix[k]

        # Elimination coefficients
        for i in range(k + 1, g):
            matrix[i][k] /= matrix[k][k]

        # Update the remaining submatrix
        for j in range(k + 1, g):
            for i in range(k + 1, g):
                matrix[i][j] -= matrix[i][k] * matrix[k][j]

    # Transform right‑hand side according to pivot swaps
    for k in range(g - 1):
        sk = s[k]
        if sk > k:
            vecb[k], vecb[sk] = vecb[sk], vecb[k]

    # Forward substitution (L y = b)
    for k in range(1, g):
        for j in range(k):
            vecb[k] -= matrix[k][j] * vecb[j]

    # Back substitution (U x = y)
    for k in range(g - 1, -1, -1):
        for j in range(k + 1, g):
            vecb[k] -= matrix[k][j] * vecb[j]
        vecb[k] /= matrix[k][k]

    # Copy result to vecx
    for k in range(g):
        vecx[k] = vecb[k]


def main():
    # 1. Discretization
    nj = 101
    n = nj
    nt = 100
    dx = 1.0 / (nj - 1)

    # 2. Solution vectors
    u_new = [0.0] * nj
    u_old = [0.0] * nj

    # 3. Matrix and RHS (allocate as 2D list for clarity)
    matrix = [[0.0] * n for _ in range(n)]
    vecb = [0.0] * n
    vecx = [0.0] * n

    # 4. Parameters
    alpha = 1.0
    dt = 0.001          # time step size (overrides previous value)
    Ne = alpha * dt / (dx * dx)

    # 5. Boundary conditions
    u_bc_l = 3.0
    u_bc_r = -1.0
    u_new[0] = u_old[0] = u_bc_l
    u_new[nj - 1] = u_old[nj - 1] = u_bc_r

    # 6. Open output file
    out_file = open("out.csv", "w")

    # 7. Time loop
    for t in range(nt):
        # Assemble matrix and right‑hand side (implicit Euler)
        for i in range(n):
            vecb[i] = u_old[i]
            for j in range(n):
                matrix[i][j] = 0.0
                if i == j:
                    matrix[i][j] = 1.0 + 2.0 * Ne
                elif abs(i - j) == 1:
                    matrix[i][j] = -Ne

        # Apply Dirichlet boundary conditions (rows 0 and n-1 set to identity)
        for i in (0, n - 1):
            for j in range(n):
                matrix[i][j] = 0.0
            matrix[i][i] = 1.0
            # vecb[i] already holds u_old[i] which equals the boundary value

        # Solve the linear system
        gauss(matrix, vecb, vecx, n)

        # Copy solution to u_new
        for i in range(n):
            u_new[i] = vecx[i]

        # Write current solution to file
        for ix in range(nj):
            x = dx * ix
            out_file.write(f"{x},{u_new[ix]}\n")

        # Update old solution for the next time step (interior only)
        for i in range(1, nj - 1):
            u_old[i] = u_new[i]

    out_file.close()


if __name__ == "__main__":
    main()