/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize){
    int *output = malloc(sizeof(int)*numsSize);
    output[0] = nums[0];
    for (int i = 1; i < numsSize; i++){
        output[i] = nums[i] + output[i-1];
    }
    *returnSize = numsSize;
    return output;
    
}
