#include <iostream>

using namespace std;

int main(){

	int number = 111;
	int temp = number;

	int *arr;
	arr = new int [3];

	int sum;
	int i = 0;

	while(1>0){
		arr[2] = number / 100;
		number = number % 100;
		arr[1] = number / 10;
		number = number % 10;
		arr[0] = number / 1;
		number = number % 1;

		sum = arr[0]*arr[0] + arr[1]*arr[1] + arr[2]*arr[2];


		if(sum == 1000 || i == 888){
			cout << arr[0] << " " << arr[1] << " " << arr[2];
			
		}
		i = i + 1;
		number = temp + i;
		cout << arr[0] << " " << arr[1] << " " << arr[2] << "\n";
		cout << number << "\n";
	}


 

	return 0;
}