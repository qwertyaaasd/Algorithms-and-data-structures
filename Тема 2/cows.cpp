#include <iostream>
#include <vector>

using namespace std;

bool boxes(vector <int> & arr, int & k, int & m) {
	int cnt = 1;
	int first = arr[0];
	for (int i=1; i < arr.size(); i++) {
		if (arr[i] - first >= m) {
			cnt++;
			first = arr[i];
		}
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
	r = arr[arr.size()-1] - arr[0] + 1;
	while (r - l > 1) {
		m = (l + r) / 2;
		if (boxes(arr, k, m)){
			l = m;
		}
		else {
			r = m;
		}
	}
	
	cout << l;
}
