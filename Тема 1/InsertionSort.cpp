#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

void InsertionSort(vector<int>& arr)
{
	int y, j;
	
	for (int i=1; i < arr.size(); i++){
		y = arr[i];
		j = i;
		while (j >= 1 and arr[j-1] > y){
			arr[j] = arr[j-1];
			j--;
		}
		arr[j] = y;
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
	
	InsertionSort(arr);
	
	return 0;
}
