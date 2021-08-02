/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* buildArray(int* nums, int numsSize, int* returnSize){
    int *output = malloc(sizeof(int)*numsSize);
    for (int i=0; i < numsSize; i++){
        output[i] = nums[nums[i]];
    }    
    *returnSize = numsSize;
    return output;
}
