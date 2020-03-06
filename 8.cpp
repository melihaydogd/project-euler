#include <iostream>

using namespace std;

int main(){
	int *arr;
	arr = new int [1000];

	for(int i = 0; i < 1000; i++){
		cin >> arr[i];
	}

	long int max = 0;
	long int mult = 1;

	for(int i = 0; i < 996; i++){
		for(int j = 0; j < 13; j++){
		mult = mult * arr[i+j];
		}
		if(mult > max){
			max = mult;
		}
		mult = 1;
	}
	cout << max;

	return 0;
}