#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main()
{
	system("chcp 1251");

	int x, n;
	int cnt = 0;
	vector<int> arr;
	
	cin >> n;
	
	while (cin >> x){
		arr.push_back(x);
	}
	
	for (int i=0; i < n; i++){
		for (int j=0; j < n - 1; j++){
			if (arr[j+1] < arr[j]){
				swap(arr[j+1], arr[j]);
				cnt++;
			}
		}
	}

	cout << cnt << endl;
	
	return 0;
}