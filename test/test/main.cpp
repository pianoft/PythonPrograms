#include<bits/stdc++.h>
#define ll long long//通常ここを変更しないように
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
void Cond(int g){if(g)p("YES")else p("NO")rt;}
void cond(int g){if(g)p("Yes")else p("No")rt;}
ll gcd(ll a,ll b){if(a<b)swap(a,b);if(a%b==0)rt b;gcd(b,a%b);}
str su="0123456789";
str m1="abcdefghijklmnopqrstuvwxyz";
str m2="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
map<char,ll>m5;
typedef pair<ll,ll> P;
const ll INF=(ll)1e17;
ll t1=0,t2=0,t3=0,t4=0,t5=0,t6=0,t7=0,t8=0;
set<P> pst;
set<char> cst;
void di(){m5['a']=0;
	m5['b']=1;
	m5['c']=2;
	m5['d']=3;
	m5['e']=4;
	m5['f']=5;
	m5['g']=6;
	m5['h']=7;
	m5['i']=8;
	m5['j']=9;
	m5['k']=10;
	m5['l']=11;
	m5['m']=12;
	m5['n']=13;
	m5['o']=14;
	m5['p']=15;
	m5['q']=16;
	m5['r']=17;
	m5['s']=18;
	m5['t']=19;
	m5['u']=20;
	m5['v']=21;
	m5['w']=22;
	m5['x']=23;
	m5['y']=24;
	m5['z']=25;
}
typedef std::vector<ll> vl;
typedef pair<ll,ll> P;
typedef pair<ll,P> 	P2;
typedef struct edge2{P to;ll cost;}EDGE2;
typedef struct edge1{ll to,cost;}EDGE;
vector<vector<EDGE>>G(1e6);
ll n,m,mx=-INF,mn=INF,ct=0;
bl used[(ll)1e9];
ldb pi=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679;
ll W;
vector<vector<ll>>g2(1e5);
vector<vector<ll>>g3(1e5);
vector<ll> vv(1e5);
vector<ll> w(1e5);
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; } return 0; }
int main(){//swap(配列１,配列２)
	//a.erase(a.begin()+5),a.insert(a.begin()+3,tmp)
	ios_base::sync_with_stdio(0); cin.tie(0);
clock_t start = clock();//時間測定
cin>>n;
rp(i,1,n){
rp(j,i+1,n){
t1=i+j;
ct+=(t1==n);
}}
p(ct)



return 0;
clock_t end = clock();//時間測定
const double time = static_cast<double>(end - start) / CLOCKS_PER_SEC * 1000.0;//時間測定
//printf("time %lf[ms]\n", time);//時間測定
return 0;
}//main