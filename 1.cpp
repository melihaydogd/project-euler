#include <iostream>

using namespace std;

int main(){
	int temp = 0;
	for(int i = 1; i < 1000; i++){
		if(i % 3 == 0){
			temp = temp + i;
		}else if(i % 5 == 0){
			temp = temp + i;
		}
	}
	cout << temp;
	return 0;
}
