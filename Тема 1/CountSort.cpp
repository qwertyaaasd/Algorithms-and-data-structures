#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

void CountSort(vector<int>& arr, int max)
{
	int counter[max+1] = {};
	
	for (int i=0; i < arr.size(); i++){
		counter[arr[i]]++;
	}
	
	int ind = 0;
	for (int i=0; i < max+1; i++){
		while (counter[i] > 0){
			arr[ind] = i;
			counter[i]--;
			ind++;
		}
	}
	
	for (int i=0; i < arr.size(); i++){
		cout << arr[i] << " ";
	}
}

int main()
{
	int x;
	int max = 100;
	vector<int> arr;
	
	while (cin >> x){
		arr.push_back(x);
	}
	
	CountSort(arr, max);
	
	return 0;
}
