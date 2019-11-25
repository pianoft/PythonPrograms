#include<bits/stdc++.h>
#define ll long long//
#define rp(i,a,b) for(ll i=a;i<b;i++)
#define r(i,n) for(ll i=0;i<n;i++)
#define rt return
#define db double
#define ldb long double
#define vd void
#define p(x) cout<<(x)<<endl;
#define ce continue;
#define bl bool
#define r0 rt 0;
#define r1 rt 1;
#define elif else if
#define bk break;
#define A p("A")
#define B p("B")
#define C p("C")
#define D p("D")
#define E p("E")
#define F p("F")
#define S(a) sort(a.begin(),a.end());
#define R(a) reverse(a.begin(),a.end());
#define cl cout<<endl;
#define pb(x) push_back(x);
#define str string
using namespace std;
typedef pair<ll,ll> P;
const ll INF=(ll)1e17;
ll t1=0,t2=0,t3=0,t4=0,t5=0,t6=0,t7=0,t8=0,g=0,ans=0;
ll n=0,m=0,k=0,mx=-INF,mn=INF,ct=0;
typedef pair<ll,ll> P;
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return 1; } return 0; }


ll h,w;
bl a[600][600];
bl b[600][600];
ll c[600][600];
bl usd[600][600];
vd bfs(ll i,ll j){
    c[i][j]=0;
    memset(usd,0,sizeof(usd));
    queue<pair<P,ll>>que;
    que.push({{i,j},0});
    while(!que.empty()){
    pair<P,ll> q=que.front();
    i=q.first.first;
    j=q.first.second;
    ll dst=q.second;
    que.pop();
    usd[i][j]=1;
    //cout<<"settedd"<<i<<" "<<j<<" "<<dst<<endl;
    if(++ct>100)bk
    for(int s=-1;s<=1;s++){
    for(int t=-1;t<=1;t++){
        t1=abs(s);t2=abs(t);
        if((t1+t2)==2||(t1+t2)==0)ce
        t1=s;t2=t;
        if(((t1+i)<0)||((t1+i)>h)||((t2+j)<0)||((t2+j)>w))ce
        
        if(usd[t1+i][t2+j])ce
        if(a[t1+i][t2+j])ce
       if(c[t1+i][t2+j]>(dst+1)){
            c[t1+i][t2+j]=dst+1;
            que.push({{t1+i,t2+j},dst+1});
       //     cout<<t1+i<<","<<t2+j<<" "<<dst+1<<"hsbnaded"<<endl;
        }
    }//rep
   }//rep

}//whi

}
int main(){//swap(ary１,ary２)
    //a.erase(a.begin()+5),a.insert(a.begin()+3,tmp)
    ios_base::sync_with_stdio(0); cin.tie(0);
clock_t start = clock();//timecalc
cin>>h>>w;
r(i,h){
str s;
cin>>s;
r(j,w){
    if(s[j]=='#')a[i+1][j+1]=1;
    else a[i+1][j+1]=0;
    }
}

rp(i,0,600){
rp(j,0,600){
    c[i][j]=INF;
}}
rp(i,1,h+1){
rp(j,1,w+1){
if(a[i][j])bfs(i,j);
}}
vector<str>s2;
rp(i,1,h+1){
    str s="";
rp(j,1,w+1){
s+=to_string(c[i][j]);
if(j!=w)s+=" ";
}
s2.pb(s)
}
r(i,h){cout<<(s2[i])<<endl;}




return 0;
clock_t end = clock();//
const double time = static_cast<double>(end - start) / CLOCKS_PER_SEC * 1000.0;//timecalc
//printf("time %lf[ms]\n", time);//
return 0;
}//main
