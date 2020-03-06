#include <iostream>

using namespace std;

int main(){
	
	int counter = 0;
	int flag = 0;
	int remember;
	
	int *arr;
	arr = new int [40];
	
	arr[0] = 0;
	arr[1] = 1;
	
	while(1 > 0){
		arr[2+counter] = arr[1+counter] + arr[0+counter];
		for(int j = 0 ; j<40; j++){
			cout << arr[j] << " ";
			if(arr[j] > 4000000){
				flag = 1;
				remember = j;
				break;
			}
		}
		if(flag == 1){
			break;
		}
		cout << "\n";
		counter = counter + 1;
	}
	int temp = 0;
	for(int i = 0; i < remember; i++){
		if(arr[i] % 2 == 0){
			temp = temp + arr[i];
		} 
	}
	cout << temp;
	
	return 0;
}
