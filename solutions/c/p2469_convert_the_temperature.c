double* convertTemperature(double celsius, int* returnSize){
    *returnSize = 2;
    double *retarr = malloc((*returnSize)*sizeof(double));
    retarr[0] = celsius + 273.15;
    retarr[1] = (celsius*1.80)+32;
    return retarr;
}
