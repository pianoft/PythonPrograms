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
void Cond(int g){if(g)p("YES")else p("NO")rt;}
void cond(int g){if(g)p("Yes")else p("No")rt;}
ll gcd(ll a,ll b){if(a<b)swap(a,b);if(a%b==0)rt b;gcd(b,a%b);}
str su="0123456789";
str m1="abcdefghijklmnopqrstuvwxyz";
str m2="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
map<char,ll>m5;
typedef pair<ll,ll> P;
const ll INF=(ll)1e17;
ll t1=0,t2=0,t3=0,t4=0,t5=0,t6=0,t7=0,t8=0,g=0,ans=0;
ll n=0,m=0,k=0,mx=-INF,mn=INF,ct=0;
ll tmp=0,tmp1=0,tmp2=0,tmp3=0,tmp4=0;
set<P> pst;
set<ll>st,st1,st2;
set<char> cst;
ll powmod(ll a,ll b,ll x){//(a^b)modx
    if(!b)r1
    if(!(b%2)){//B
        ll t=powmod(a,b/2,x);
        rt t*t%x;
    }
    rt ((a)*powmod(a,b-1,x))%x;
}
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
map<ll,ll>mp,mp1,mp2,mp3;
typedef std::vector<ll> vl;
typedef pair<ll,ll> P;
typedef pair<ll,P>  P2;
typedef struct edge2{P tos;ll cost;}EDGE2;
typedef struct edge1{ll to,cost;}EDGE;
bl used[(ll)1e9];
const ll M=(ll)1e9+7;
ll fac[1000007],finv[1000007],inv[1000007];
void initcmb(){
    fac[0]=fac[1]=1;
    finv[0]=finv[1]=1;
    inv[1]=1;
    for(int i=2;i<1000007;i++){
        fac[i]=fac[i-1]*i%M;
        inv[i]=M-inv[M%i]*(M/i)%M;
        finv[i]=finv[i-1]*inv[i]%M;
    }
}
ll cmb(ll n,ll k){
    if(n<k)return 0;
    if(n<0 || k<0)return 0;
    return fac[n]*(finv[k]*finv[n-k]%M)%M;
}
ldb pi=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679;
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; r1 } r0 }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; r1 } r0 }
ll TLE=0;
vd tle(){TLE++;if(TLE>(ll)1e8*2){p("ALERT ALERT ALERT ALERT")}rt;}
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
di();
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
