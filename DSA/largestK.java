import java.util.Arrays;

public class largestK {

	public static void main(String[] args) {
		System.out.println(getLargestK(new int[] {3, 2, -2, 5, -3}));
		System.out.println(getLargestK(new int[] {1, 2, 3, -4}));
	}
	
	public static int getLargestK(int[] A) { 
		Arrays.sort(A); 
		int l = 0, r = A.length -1; 
		while (l < r) {
			if (A[l] == - A[r]) return A[r];
			if (-A[l] > A[r]) {
				l++; 
			} else {
				r--;
			}
		}
		return 0; 
	}
}
