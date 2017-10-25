#include <iostream>
using namespace std;

int main(){
	char s;
	cin>>s;
	int a = 0;
	int b = 0;
	for(int i=0; i<s.length(); i++){
		if (s[i]=='a'){
			a++;
		}
		else{
			b++;
		}
	}
	if (a<b){
		cout<<a;
	}
	else{
		cout<<b;
	}
	return 0;
}