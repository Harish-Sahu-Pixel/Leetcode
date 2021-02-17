'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).

n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).

Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
'''

class Solution {
public:
    int maxArea(vector<int>& height) 
    {
        vector<int>::iterator i,j,k;
        i=height.begin();
        j=height.end()-1;
        int max = ((j-i)*min(i,j));
        if(height.size()==2)
        {
            return max;
        }
        while(i<j)
        {
            if(*i<*j)
            {
                i++;
                if(((j-i)*min(i,j))>max)
                {
                    max=((j-i)*min(i,j));
                } 
            }
            else
            {
                j--;
                if(((j-i)*min(i,j))>max)
                {
                    max=((j-i)*min(i,j));
                }
            }
        }
        return max;
    }
public:
    int min(vector<int>::iterator a,vector<int>::iterator b)
    {
        if(*a<*b)
        {
            return *a;
        }
        else
        {
            return *b;
        }
    }
};
