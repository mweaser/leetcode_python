class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++){
            int difference = target - nums[i]; 
            for (int j =  i + 1; j < nums.size(); j++){
                if (nums[j] == difference){
                    vector<int> a = {i, j};
                    return a;
                }
            }
        }
        return nums;
    }
};