import sys
import numpy as np
import glob
import matplotlib.pyplot as plt
import os

print(sys.version)
print(sys.executable)
cwd = os.getcwd()

path = cwd + "/*.dta"
print(path)
plt.clf()
files = glob.glob(path)
index = 0
rawOCP = []
rawOCP = np.array(rawOCP)
rawPolar = []
rawPolar = np.array(rawPolar)

ymax = -0.4
ymin = -1.2
OCPymax = -0.5
OCPymin = -1.5
# in cm
Dia = 80*10**(-4)
Area = 3.14*(Dia/2)**2
for fle in files:
    n = os.path.basename(fle).split(".dta")[0]
    print(n)
    with open(fle) as infile:
        OCP = []
        Polar = []
        indata = infile.readlines()

        for line in indata:
            if line.startswith("\t"):
                line = line.split()
                if len(line) == 6:
                    OCP.append(line)

                elif len(line) == 9:
                    Polar.append(line)

        OCP = np.array(OCP)
        OCP = np.delete(OCP, 0, 0)
        OCP = np.delete(OCP, 0, 0)

        OCP = np.delete(OCP, 5, 1)
        OCP = OCP.astype(np.float)
        print(OCP.shape)
        Polar = np.array(Polar)
        Polar = np.delete(Polar, 0, 0)
        Polar = np.delete(Polar, 8, 1)
        Polar = np.array(Polar.astype(np.float))

        plt.figure(1)
        plt.xlabel('Time (s)')
        plt.ylabel('E vs.SCE (V)')
        plt.plot(OCP[:, 1], OCP[:, 2], label=str(n))
        plt.legend()
        plt.title('OCP')
        plt.ylim(OCPymin, OCPymax)
        plt.figure(2)
        plt.plot(np.absolute(Polar[:, 3])/Area, Polar[:, 2], label=str(n))
        plt.legend()
        plt.xscale('log')
        plt.xlabel('i mA/cm^2')
        plt.ylabel('E vs.SCE (V)')
        plt.title('Polarization')
        plt.ylim(ymin, ymax)

    infile.close()
    index = index+1

fig = plt.figure(1)
fig.savefig("OCP.png")

fig = plt.figure(2)
fig.savefig("Polar.png")
