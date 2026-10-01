#include <iostream>
#include <cmath>

using namespace std;

bool good(long long & w, long long & h, long long & n, long long & m) {
	long long cnt = (long long)(m / w) * (m / h);
	return cnt >= n;
}


main () {
	long long w, h, n;
	cin >> w >> h >> n;

	long long l = 0;
	long long r = 0;
	if (w < h) {
		r = h * n;
	}
	else {
		r = w * n;
	}
	while (r - l > 1) {
		long long m = (l + r) / 2;
		if (good(w, h, n, m)) {
			r = m;
		}
		else {
			l = m;
		}
	}
	
	cout << r;
}
