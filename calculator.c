#include <stdio.h>
#include <math.h>

// Function declarations
double calculateAcceleration(double v, double u, double t);
double calculateVelocity(double u, double a, double t);
double calculateDisplacement(double u, double t, double a);
double calculateForce(double m, double a);
double calculateKineticEnergy(double m, double v);
double calculatePotentialEnergy(double m, double g, double h);
double calculateWork(double f, double d);
double calculatePower(double w, double t);
double calculateMomentum(double m, double v);
double calculateFrequency(double T);
double evaluateExpression(double a, double b, double c); // (a + b) * c
double calculateSinTheta(double theta);
double calculateCosTheta(double theta);

int main() {
    int choice;
    double u, v, a, t, m, f, d, g = 9.8, h, w, T, theta, b, c;

    do {
        printf("\n--- Formula Solver Menu ---\n");
        printf("1. Acceleration (a = (v - u) / t)\n");
        printf("2. Final Velocity (v = u + a * t)\n");
        printf("3. Displacement (s = ut + 0.5at^2)\n");
        printf("4. Force (F = m * a)\n");
        printf("5. Kinetic Energy (KE = 0.5 * m * v^2)\n");
        printf("6. Potential Energy (PE = m * g * h)\n");
        printf("7. Work (W = F * d)\n");
        printf("8. Power (P = W / t)\n");
        printf("9. Momentum (p = m * v)\n");
        printf("10. Frequency (f = 1 / T)\n");
        printf("11. Expression: (a + b) * c\n");
        printf("12. Sin(theta)\n");
        printf("13. Cos(theta)\n");
        printf("0. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter initial velocity (u): "); scanf("%lf", &u);
                printf("Enter final velocity (v): "); scanf("%lf", &v);
                printf("Enter time (t): "); scanf("%lf", &t);
                printf("Acceleration = %.2lf\n", calculateAcceleration(v, u, t));
                break;
            case 2:
                printf("Enter initial velocity (u): "); scanf("%lf", &u);
                printf("Enter acceleration (a): "); scanf("%lf", &a);
                printf("Enter time (t): "); scanf("%lf", &t);
                printf("Final Velocity = %.2lf\n", calculateVelocity(u, a, t));
                break;
            case 3:
                printf("Enter initial velocity (u): "); scanf("%lf", &u);
                printf("Enter time (t): "); scanf("%lf", &t);
                printf("Enter acceleration (a): "); scanf("%lf", &a);
                printf("Displacement = %.2lf\n", calculateDisplacement(u, t, a));
                break;
            case 4:
                printf("Enter mass (m): "); scanf("%lf", &m);
                printf("Enter acceleration (a): "); scanf("%lf", &a);
                printf("Force = %.2lf\n", calculateForce(m, a));
                break;
            case 5:
                printf("Enter mass (m): "); scanf("%lf", &m);
                printf("Enter velocity (v): "); scanf("%lf", &v);
                printf("Kinetic Energy = %.2lf\n", calculateKineticEnergy(m, v));
                break;
            case 6:
                printf("Enter mass (m): "); scanf("%lf", &m);
                printf("Enter height (h): "); scanf("%lf", &h);
                printf("Potential Energy = %.2lf\n", calculatePotentialEnergy(m, g, h));
                break;
            case 7:
                printf("Enter force (F): "); scanf("%lf", &f);
                printf("Enter distance (d): "); scanf("%lf", &d);
                printf("Work = %.2lf\n", calculateWork(f, d));
                break;
            case 8:
                printf("Enter work (W): "); scanf("%lf", &w);
                printf("Enter time (t): "); scanf("%lf", &t);
                printf("Power = %.2lf\n", calculatePower(w, t));
                break;
            case 9:
                printf("Enter mass (m): "); scanf("%lf", &m);
                printf("Enter velocity (v): "); scanf("%lf", &v);
                printf("Momentum = %.2lf\n", calculateMomentum(m, v));
                break;
            case 10:
                printf("Enter time period (T): "); scanf("%lf", &T);
                printf("Frequency = %.2lf\n", calculateFrequency(T));
                break;
            case 11:
                printf("Enter value for a: "); scanf("%lf", &a);
                printf("Enter value for b: "); scanf("%lf", &b);
                printf("Enter value for c: "); scanf("%lf", &c);
                printf("Result = %.2lf\n", evaluateExpression(a, b, c));
                break;
            case 12:
                printf("Enter angle in degrees: "); scanf("%lf", &theta);
                printf("Sin(%.2lf°) = %.4lf\n", theta, calculateSinTheta(theta));
                break;
            case 13:
                printf("Enter angle in degrees: "); scanf("%lf", &theta);
                printf("Cos(%.2lf°) = %.4lf\n", theta, calculateCosTheta(theta));
                break;
            case 0:
                printf("Exiting program.\n");
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    } while (choice != 0);

    return 0;
}

// Function definitions
double calculateAcceleration(double v, double u, double t) { return (v - u) / t; }
double calculateVelocity(double u, double a, double t) { return u + a * t; }
double calculateDisplacement(double u, double t, double a) { return u * t + 0.5 * a * t * t; }
double calculateForce(double m, double a) { return m * a; }
double calculateKineticEnergy(double m, double v) { return 0.5 * m * v * v; }
double calculatePotentialEnergy(double m, double g, double h) { return m * g * h; }
double calculateWork(double f, double d) { return f * d; }
double calculatePower(double w, double t) { return w / t; }
double calculateMomentum(double m, double v) { return m * v; }
double calculateFrequency(double T) { return 1.0 / T; }
double evaluateExpression(double a, double b, double c) { return (a + b) * c; }
double calculateSinTheta(double theta) { return sin(theta * m_pi / 180.0); }
double calculateCosTheta(double theta) { return cos(theta * M_PI / 180.0); }
