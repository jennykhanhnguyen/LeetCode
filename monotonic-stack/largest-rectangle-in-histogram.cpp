class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        int arrl[n];
        int arrr[n];
        long long dp[n];
        memset(dp, 0, sizeof(dp));
        stack<int> st;

        for (int i = 0; i < n; ++i)
        {
            while (!st.empty() && heights[st.top()] >= heights[i])
                st.pop();
            int ans = -1;
            if (!st.empty())
                ans = st.top();
            arrl[i] = ans;
            st.push(i);
        }

        while (!st.empty())
            st.pop();

        for (int i = n-1 ; i >= 0; --i)
        {
            while (!st.empty() && heights[st.top()] >= heights[i])
                st.pop();
            int ans = n;
            if (!st.empty())
                ans = st.top();
            arrr[i] = ans;
            st.push(i);
        }
        int maxval = -1;
        for (int i = 0; i < n; i++)
        {
            dp[i] = 1ll*heights[i]*(arrr[i]-arrl[i]-1);
            if (dp[i] > maxval)
                maxval = dp[i];
        }
        
        return maxval;
    }
};