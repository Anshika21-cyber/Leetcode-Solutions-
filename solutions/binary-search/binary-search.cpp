class Solution {
public:
    // #include <algorithm>
    int search(vector<int>& nums, int target) {
    //     auto it = find(nums.begin(), nums.end(), target);
    //     return it;
    // return -1;
    // }
// };

        
        for(int i=0;i<nums.size();i++){
            if(nums[i]==target){
                return i;
                
            }
        }
        return -1 ;
    }
     
};


