#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;

int main(){
ll n;
cin>>n;
for (int i=1;i<=9;i++){
for(int j=i;j<=9;j++){
if( (i*j)==n){
cout<<"Yes"<<endl;return 0;
}
}}
cout<<"No"<<endl;
return 0;


}









