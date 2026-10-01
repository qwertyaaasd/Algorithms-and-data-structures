#include <iostream>
#include <vector>

using namespace std;

bool good(vector <int> & arr, int & k, int & m) {
	int cnt = 0;
	for (int i=0; i < arr.size(); i++) {
		cnt = cnt + arr[i] / m;
	}
	
	return cnt >= k;
}


main () {
	int l, r, m;
	int n, k, x;
	vector <int> arr;
	cin >> n >> k;
	while (cin >> x) {
		arr.push_back(x);
	}
	
	l = 0;
	r = 10000001;
	while (r - l > 1) {
		m = (l + r) / 2;
		if (good(arr, k, m)) {
			l = m;
		}
		else {
			r = m;
		}
	}
	
	cout << l;
}
