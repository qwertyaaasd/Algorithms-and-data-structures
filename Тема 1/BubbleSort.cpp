#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

void BubbleSort(vector<int>& arr)
{
	for (int i=0; i < arr.size(); i++){
		for (int j=0; j < arr.size() - 1; j++){
			if (arr[j+1] > arr[j]){
				swap(arr[j+1], arr[j]);
			}
		}
	}
	
	for (int i=0; i < arr.size(); i++){
		cout << arr[i] << " ";
	}
	
	cout << endl;
}

int main()
{
	system("chcp 1251");

	int x;
	vector<int> arr;
	
	while (cin >> x){
		arr.push_back(x);
	}
	
	BubbleSort(arr);
	
	return 0;
}
