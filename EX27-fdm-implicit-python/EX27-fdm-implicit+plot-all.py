import math
import matplotlib.pyplot as plt
import numpy as np

def gauss(matrix, vecb, vecx, g):
    """
    Gaussian elimination with partial pivoting.
    Modifies matrix and vecb in place, stores solution in vecx.
    """
    s = [0] * (g - 1)          # pivot row indices

    # LU factorisation
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


def plot_results(filename, nj, nt):
    """
    Reads the output CSV file and produces three plots:
      - final temperature profile,
      - space‑time colour map,
      - overlay of profiles at selected time steps.
    """
    # Read all data points
    data = np.loadtxt(filename, delimiter=',')
    # data has shape (nt * nj, 2)  -> columns: x, u
    x_vals = data[:, 0]
    u_vals = data[:, 1]

    # Reshape into time steps (each block of nj lines is one time step)
    u_time = u_vals.reshape(nt, nj)
    x_grid = x_vals[:nj]   # x coordinates (same for all time steps)

    plt.figure(figsize=(15, 5))

    # ---- 1. Final profile ----
    plt.subplot(1, 3, 1)
    plt.plot(x_grid, u_time[-1, :], 'b-o', markersize=4)
    plt.xlabel('x')
    plt.ylabel('u')
    plt.title(f'Final profile (t = {nt} steps)')
    plt.grid(True)

    # ---- 2. Space‑time contour ----
    plt.subplot(1, 3, 2)
    X, T = np.meshgrid(x_grid, np.arange(nt))
    plt.pcolormesh(X, T, u_time, shading='auto', cmap='viridis')
    plt.colorbar(label='u')
    plt.xlabel('x')
    plt.ylabel('Time step')
    plt.title('Space‑time evolution')

    # ---- 3. Overlay of selected time steps ----
    plt.subplot(1, 3, 3)
    # Choose which steps to plot (e.g., every 10th step)
    steps_to_plot = range(0, nt, max(1, nt // 10))   # at most ~10 lines
    for step in steps_to_plot:
        plt.plot(x_grid, u_time[step, :], label=f'step {step}')
    plt.xlabel('x')
    plt.ylabel('u')
    plt.title('Evolution at selected time steps')
    plt.legend(loc='best')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def main():
    # 1. Discretisation
    nj = 101
    n = nj
    nt = 100
    dx = 1.0 / (nj - 1)

    # 2. Solution vectors
    u_new = [0.0] * nj
    u_old = [0.0] * nj

    # 3. Matrix and RHS (2D list for clarity)
    matrix = [[0.0] * n for _ in range(n)]
    vecb = [0.0] * n
    vecx = [0.0] * n

    # 4. Parameters
    alpha = 1.0
    dt = 0.001               # time step size
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

        # Write current solution to file (one line per spatial point)
        for ix in range(nj):
            x = dx * ix
            out_file.write(f"{x},{u_new[ix]}\n")

        # Update old solution for the next time step (interior only)
        for i in range(1, nj - 1):
            u_old[i] = u_new[i]

    out_file.close()

    # 8. Plot the results
    plot_results("out.csv", nj, nt)


if __name__ == "__main__":
    main()