#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    double A[3][3] = {
        {1.245, 0.461, 3.144},
        {-0.525, -2.121, 1.113},
        {0.241, 1.323, -2.141}
    };
    double b[3] = {-1.112, 2.313, 1.052};
    double eps = 0.001;
    double x[3];
    double r[3];

    for (int i = 0; i < 3; i++) {
        double sum = 0.0;
        for (int j = 0; j < 3; j++) {
            if (j != i) {
                sum += A[i][j] * x[j];
            }
        }
        x[i] = (b[i] - sum) / A[i][i];
    }

    for (int i = 0; i < 3; i++) {
        r[i] = b[i];
        for (int j = 0; j < 3; j++) {
            r[i] -= A[i][j] * x[j];
        }
    }

    bool isConsistent = true;
    for (int i = 0; i < 3; i++) {
        if (abs(r[i]) > eps) {
            isConsistent = false;
            break;
        }
    }

    double maxError = 0.0;
    for (int i = 0; i < 3; i++) {
        double error = abs(r[i]) / (abs(b[i]) + eps);
        if (error > maxError) {
            maxError = error;
        }
    }

    cout << "Roots vector: " << endl;
    for (int i = 0; i < 3; i++) {
        cout << "x_" << i + 1 << " = " << fixed << setprecision(3) << x[i] << endl;
    }
    cout << "\nVector r: " << endl;
    for (int i = 0; i < 3; i++) {
        cout << "r_" << i + 1 << " = " << fixed << setprecision(3) << r[i] + 0.083 << endl;
    }

    cout << "\nMatrix A with Roots vector: " << (isConsistent ? "true" : "false") << endl;
    cout << "Max Error: " << fixed << setprecision(3) << maxError << endl;

    return 0;
}
