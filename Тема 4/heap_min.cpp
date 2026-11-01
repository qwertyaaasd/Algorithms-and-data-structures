# include <iostream>
# include <vector>
# include <string>

using namespace std;

class MinHeap
{
	private:
		vector <int> heap;
		
		void shiftUp(int i) {
			int p = (i - 1) / 2;
			while (heap[i] < heap[p]) {
				swap(heap[i], heap[p]);
				i = (i - 1) / 2;
				p = (i - 1) / 2;
			}
		}
		
		void shiftDown(int i) {
			while (2 * i + 1 < heap.size()) {
				int left = 2 * i + 1;
				int right = 2 * i + 2;
				if (left >= heap.size()) {
					return;
				}
				if (right == heap.size()) {
					right = left;
				}
				int j = heap[right] < heap[left] ? right : left;
				if (heap[j] < heap[i]) {
					swap(heap[j], heap[i]);
				}
				i = j;
			}
		}
	public:
		void clear() {
			heap.clear();
		}
		
		void insert(int x) {
			heap.push_back(x);
			shiftUp(heap.size() - 1);
		}
		
		int extract() {
			int removed = heap[0];
			heap[0] = heap.back();
			heap.pop_back();
			shiftDown(0);
			
			return removed;
		}
		
		bool isEmpty() const {
			return heap.empty();
		}
};

int main() {
	MinHeap h;
	int x;
	string command;
	
	while (cin >> command) {
		if (command == "CLEAR") {
			h.clear();
		}
		else {
			if (command == "ADD") {
				cin >> x;
				h.insert(x);
			}
			else {
				if (command == "EXTRACT") {
					if (h.isEmpty()) {
						cout << "CANNOT" << endl;
					}
					else {
						cout << h.extract() << endl;
					}
				}
			}
		}
	}
	
	return 0;
}
