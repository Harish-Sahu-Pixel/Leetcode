/*
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 

X can be placed before L (50) and C (100) to make 40 and 90. 

C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
*/

class Solution {
public:
    int romanToInt(string s) 
    {
        int num=0;
        string::iterator it;
        it=s.begin();
        while(it!=s.end())
        {
            if(*it=='M')
            {
                num+=1000;
                it++;
            }
            else if(*it=='C'&&*(it+1)=='M')
            {
                num+=900;
                it+=2;
            }
            else if(*it=='D')
            {
                num+=500;
                it++;
            }
            else if(*it=='C'&&*(it+1)=='D')
            {
                num+=400;
                it+=2;
            }
            else if(*it=='C')
            {
                num+=100;
                it++;
            }
            else if(*it=='X'&&*(it+1)=='C')
            {
                num+=90;
                it+=2;
            }
            else if(*it=='L')
            {
                num+=50;
                it++;
            }
            else if(*it=='X'&&*(it+1)=='L')
            {
                num+=40;
                it+=2;
            }
            else if(*it=='X')
            {
                num+=10;
                it++;
            }
            else if(*it=='I'&&*(it+1)=='X')
            {
                num+=9;
                it+=2;
            }
            else if(*it=='V')
            {
                num+=5;
                it++;
            }
            else if(*it=='I'&&*(it+1)=='V')
            {
                num+=4;
                it+=2;
            }
            else if(*it=='I')
            {
                num+=1;
                it++;
            }
        }
        return num;
    }
};
