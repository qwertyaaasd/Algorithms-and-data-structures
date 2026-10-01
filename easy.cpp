#include <iostream>

using namespace std;

main () {
	int l, r, m;
	int n, slow, fast;
	cin >> n >> slow >> fast;
	
	int a;
	if (slow < fast) {
		a = slow;
		slow = fast;
		fast = a;
	}

	l = 0;
	r = (n - 1) * slow;
	while (r - l > 1) {
		m = (l + r) / 2;
		if (m / slow + m / fast >= n - 1) {
			r = m;
		}
		else {
			l = m;
		}
	}
	
	cout << (fast + r);
}
