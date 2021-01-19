'''
Given a string s, return the longest palindromic substring in s.
'''

class Solution {
public:
    string longestPalindrome(string s) 
    {
        string str;
        int max=0,loci=0,locj=0;
        int x=s.length();
        if(x==0)
        {
            return "";
        }
        int x1=x,x2=x;
        bool arr[x][x];
        int i=0,j=0,k=0;
        while(i<x1)
        {
            j=i+k;
            while(j<x2)
            {
                if(i==j)
                {
                    arr[i][j]=true;
                    if(j-i+1>max)
                    {
                        max=j-i+1;
                        loci=i;
                        locj=j;
                    }
                }
                else if(j-i==1)
                {
                    if(s[i]==s[j])
                    {
                        arr[i][j]=true;
                        if(j-i+1>max)
                        {
                            max=j-i+1;
                            loci=i;
                            locj=j;
                        }
                    }
                    else
                    {
                        arr[i][j]=false;
                    }
                }
                else
                {
                    if(arr[i+1][j-1]==true && s[i]==s[j])
                    {
                        arr[i][j]=true;
                        if(j-i+1>max)
                        {
                            max=j-i+1;
                            loci=i;
                            locj=j;
                        }
                    }
                    else
                    {
                        arr[i][j]=false;
                    }
                }
                i++;
                j++;
            }
            i=0;
            k++;
            x1--;
        }
        for(int i=loci;i<=locj;i++)
        {
            str.push_back(s[i]);
        }
        return str;
    }
};
