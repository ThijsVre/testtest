import numpy as np
import matplotlib.pyplot as plt

# Constantes
G = 6.67430e-11
M = 1.898e27        # Massa Jupiter
m1 = 8.93e22        # Io
m2 = 4.8e22         # Europa
dt = 5              # Tijdstap in seconden
t = 0

# Beginposities
Mx, My = 0.0, 0.0
m1x, m1y = 4.22e8, 0.0
m2x, m2y = 6.71e8, 0.0

# Beginsnelheden (loodrecht op straalvector)
vMx, vMy = 0.0, 0.0
vm1x, vm1y = 0.0, 17334.0
vm2x, vm2y = 0.0, 13740.0

# Voor grafiek
m1_traj = []
m2_traj = []

# Simulatielus
for step in range(100000):  # aantal stappen
    # Afstanden
    rMm1 = np.sqrt((Mx - m1x)**2 + (My - m1y)**2)
    rMm2 = np.sqrt((Mx - m2x)**2 + (My - m2y)**2)
    rm1m2 = np.sqrt((m2x - m1x)**2 + (m2y - m1y)**2)

    # Krachten
    FzMm1 = G * M * m1 / rMm1**2
    FzMm2 = G * M * m2 / rMm2**2
    Fzm1m2 = G * m1 * m2 / rm1m2**2

    # Krachtcomponenten
    FzMm1x = FzMm1 * (m1x - Mx) / rMm1
    FzMm2x = FzMm2 * (m2x - Mx) / rMm2
    Fzm1m2x = Fzm1m2 * (m2x - m1x) / rm1m2

    FzMm1y = FzMm1 * (m1y - My) / rMm1
    FzMm2y = FzMm2 * (m2y - My) / rMm2
    Fzm1m2y = Fzm1m2 * (m2y - m1y) / rm1m2

    # Actie-reactiekrachten
    Fzm1Mx = -FzMm1x
    Fzm2Mx = -FzMm2x
    Fzm2m1x = -Fzm1m2x

    Fzm1My = -FzMm1y
    Fzm2My = -FzMm2y
    Fzm2m1y = -Fzm1m2y

    # Totale krachtcomponenten
    FMx = FzMm1x + FzMm2x
    FMy = FzMm1y + FzMm2y

    Fm1x = Fzm1m2x + Fzm1Mx
    Fm2x = Fzm2Mx + Fzm2m1x

    Fm1y = Fzm1m2y + Fzm1My
    Fm2y = Fzm2My + Fzm2m1y

    # Versnellingen
    aMx = FMx / M * dt
    aMy = FMy / M * dt

    am1x = Fm1x / m1 * dt
    am1y = Fm1y / m1 * dt

    am2x = Fm2x / m2 * dt
    am2y = Fm2y / m2 * dt

    # Snelheden
    vMx += aMx
    vMy += aMy

    vm1x += am1x
    vm1y += am1y

    vm2x += am2x
    vm2y += am2y

    # Posities
    Mx += vMx * dt
    My += vMy * dt

    m1x += vm1x * dt
    m1y += vm1y * dt

    m2x += vm2x * dt
    m2y += vm2y * dt

    # Tijd
    t += dt

    # Opslaan voor plot
    m1_traj.append((m1x, m1y))
    m2_traj.append((m2x, m2y))

# === PLOT ===
m1_traj = np.array(m1_traj)
m2_traj = np.array(m2_traj)

plt.figure(figsize=(8, 8))
plt.plot(0, 0, 'yo', label='Jupiter')
plt.plot(m1_traj[:,0], m1_traj[:,1], 'r-', label='Io')
plt.plot(m2_traj[:,0], m2_traj[:,1], 'b-', label='Europa')
plt.axis('equal')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Simulatie van Jupiter, Io & Europa')
plt.legend()
plt.grid(True)
plt.show()

