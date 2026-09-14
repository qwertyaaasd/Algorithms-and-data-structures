#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

void SelectionSort(vector<int>& arr)
{
	int y, ind;
	
	for (int i=0; i < arr.size(); i++){
		y = arr[i];
		ind = i;
		for (int j=i+1; j < arr.size(); j++){
			if (arr[j] > y){
				y = arr[j];
				ind = j;
			}
		}
		if (i != ind){
			swap(arr[i], arr[ind]);
		}
	}
	
	for (int i=0; i < arr.size(); i++){
		cout << arr[i] << " ";
	}
}

int main()
{
	int x;
	vector<int> arr;
	
	while (cin >> x){
		arr.push_back(x);
	}
	
	SelectionSort(arr);
	
	return 0;
}
