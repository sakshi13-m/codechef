
#include <bits/stdc++.h>
#define pb push_back
#define forp(i,n) for(int i=1;i<=n;i++)
#define krsna ll t; cin>>t; while(t--) radhekrishna();
using namespace std;
using ll = long long;
using pii = pair<int,int>;
using pli = pair<ll,int>;
const int N = 2e5 + 5;
using namespace std;

int swap(ll [],ll [],ll,ll,ll);
void radhekrishna();

int main()
{
	
	krsna
	return 0;
}

void radhekrishna()
{
    ll n, k, a[N];
    bool vis[N];
    
	cin>>n>>k;
	
	forp(i,n)
	cin>>i[a];
	
	
	ll p[N];
	
	forp(i,n)
	p[i[a]] = i;
		
	vector <array<int,3>> op;
	
	for(int i=1; i<=n; i++)
	{
		i[vis] = 0;
		if(i!=i[p])
		{
			int x = i[p], y = i, z =i[a];
			if(z==x) continue;
			op.pb({y, z, x});
			swap(a,p,y, z, x);
		}
	}
	vector <pii> loop;
	for(int i=1; i<=n; i++)
	{
		if(i!=i[a] &&i[p]==i[a] && !vis[i[p]])
		{
			loop.pb({i, i[p]});
			vis[i] = vis[p[i]] = 1;
		}
	}
	if(loop.size()&1) 
	{
		puts("-1");
		return;
	}
	for(int i=0; i<loop.size(); i+=2)
	{
		int aa = loop[i].first, bb = loop[i].second, cc = loop[i+1].first, dd = loop[i+1].second;
		op.pb({bb, cc, dd});
		swap(a,p,bb, cc, dd);
		op.pb({aa, bb, cc});
		swap(a,p,aa, bb, cc);
	}
	if(op.size()>k || !is_sorted(a+1, a+n+1)) puts("-1");
	else
	{
		cout << op.size() << '\n';
		for(auto it : op)
		cout<<it[0]<<" "<<it[1]<<" "<<it[2]<<endl;
	}
}
int swap(ll a[],ll p[],ll x, ll y, ll z)
{
	assert(x!=y); assert(y!=z); assert(x!=z);
	int tmp = a[z];
	a[z] = a[y];
	p[a[y]] = z; 
	a[y] = a[x]; 
	p[a[x]] = y;
	a[x] = tmp;
	p[tmp] = x;
	
	return 0;
}
