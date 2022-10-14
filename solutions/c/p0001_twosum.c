//clearly this is bad because I don't sort the list beforehand, but 2 minute solution...
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int index1, index2;
    *returnSize = 2;
    int* retarr = (int*)malloc(sizeof(returnSize));
    for (index1 = 0; index1 < numsSize-1; index1++){
        for(index2= index1+1; index2 < numsSize; index2++){
            if (nums[index2]+nums[index1]==target){
                retarr[0] = index1;
                retarr[1] = index2;
                return retarr;
            }
        }
    }
    return -1;
}
