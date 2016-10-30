#include<iostream>
#include <stdint.h>
using namespace std;
/*
int64_t hash(string s)
{
	int64_t h = 7;
    string letters = "acdegilmnoprstuw";
    for(int32_t i=0; i < s.length(); i++) 
	{
        h = (h*37 + letters.find(s[i]));
    }
    return h;
}
*/
string hashRev(int64_t i)
{
	string s="";
	string letters = "acdegilmnoprstuw";
	int64_t mod=i%37;
	int j=7;
while(j>0)
	{
		i=i/37;
		s=letters[mod]+s;
		j--;
		mod=i%37;
	}
	return s;
}

int main()
{
	cout<<hashRev(680131659347);
	return 0;
}
