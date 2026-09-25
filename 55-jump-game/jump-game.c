bool canJump(int* nums, int numsSize) {
    int far=0;
    for(int i=0;i<numsSize;i++){
        if(i>far){
            return false;
        }
        if(far>i+nums[i]){
            far=far;
        }
        else{
            far=i+nums[i];
        }
    }
    return true;
}