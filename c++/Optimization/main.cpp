#include <iostream>
#include <fstream>
#define INFINITY 9999999999

using namespace std;

int main() {
	double next[20][20];
	double a[20][20];
	double b[20][20];

	long bo[20][20];
	double del[20][20];
	double dl[20][20];
	double o[20][20];


	ifstream innext("next.txt");
	cout << "next" << endl;
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			innext >> next[i][j];
		}
	}

	ifstream ina("a.txt");
	cout << "a" << endl;
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			ina >> a[i][j];
		}
	}

	ifstream inb("b.txt");
	cout << "b" << endl;
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			inb >> b[i][j];
		}
	}

	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			del[i][j] = 0;
			dl[i][j] = 0;
			o[i][j] = 0;
		}
	}

	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			bo[i][j] = b[i][j];
		}
	}

	double dc = 10000;
	double Oprev = INFINITY;
	double m0 = INFINITY;

	int cycles = 0;

	do {
		Oprev = m0;

		cycles++;

		for (int i = 0; i < 20; i++) {
			for (int j = 0; j < 20; j++) {
				if (bo[i][j] != 0) {

					double L = 200 * 8;
					for (int x = 0; x < 20; x++) {
						for (int y = 0; y < 20; y++) {
							if (bo[x][y] != 0) {
								double bm = bo[x][y];
								double am = a[x][y];
								if ((i == x) && (j == y)) {
									bm += dc;
								}
								del[x][y] = L / (bm - am);
							}
						}
					}

					for (int x = 1; x < 21; x++) {
						for (int y = 1; y < 21; y++) {

							double sum = 0;

							if (x == y) {
								sum = del[x - 1][y - 1];
							}
							else {
								int k = x;
								int nextK = y;
								while (k != y) {
									nextK = next[k - 1][y - 1];
									sum += del[k - 1][nextK - 1];
									k = nextK;
								}
							}

							dl[x - 1][y - 1] = sum;

						}
					}

					double Topt = 0.05;
					double sumO = 0;
					for (int x = 0; x < 20; x++) {
						for (int y = 0; y < 20; y++) {
							sumO += (dl[x][y] - Topt) * (dl[x][y] - Topt);
						}
					}
					o[i][j] = sumO;
				}
			}
		}

		int mi = 0;
		int mj = 0;
		m0 = o[mi][mj];

		for (int i = 0; i < 20; i++) {
			for (int j = 0; j < 20; j++) {
				if (o[i][j] != 0) {
					double tmp = o[i][j];
					if (tmp < m0) {
						m0 = tmp;
						mi = i;
						mj = j;
					}
				}
			}
		}

		double b = bo[mi][mj];
		bo[mi][mj] = b + dc;

		cout << "cycles =" << cycles << endl;

	} while (m0 < Oprev);

	ofstream outb0("b0.txt");
	cout << "B0" << endl;
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			cout << bo[i][j] << "\t";
			outb0 << fixed << bo[i][j] << "\t";
		}
		cout << endl;
		outb0 << endl;
	}

	ofstream outdel("del.txt");
	cout << "DEL" << endl;
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			cout << del[i][j] << "\t";
			outdel << del[i][j] << "\t";
		}
		cout << endl;
		outdel << endl;
	}

	ofstream outdl("dl.txt");
	cout << "DL" << endl;
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			cout << dl[i][j] << "\t";
			outdl << dl[i][j] << "\t";
		}
		cout << endl;
		outdl << endl;
	}

	ofstream outo("o.txt");
	cout << "O" << endl;
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			cout << o[i][j] << "\t";
			outo << o[i][j] << "\t";
		}
		cout << endl;
		outo << endl;
	}

	system("pause");
	return 0;
}
