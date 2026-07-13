class Solution {
    public int largestAltitude(int[] gain) {
        int alt=0,max=0;
        for(int x:gain){
            alt+=x;
            max=Math.max(max,alt);
        }
        return max;
    }
}