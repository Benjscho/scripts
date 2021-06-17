public class numSwaps {

	public static void main(String[] args) {
		assert(getNoSwaps("mamad") == 3); 
		assert(getNoSwaps("ntiin") == 1); 
		System.out.println(getNoSwaps("asdfdkgadsl")); 
	}

	private static int getNoSwaps(String s) { 
		char[] sc = s.toCharArray();
		if (!isJumbledPalindrome(sc)) return -1; 
		int l = 0, r = sc.length-1;
		int nb_swaps = 0; 
		while (l < r) { 
			if (sc[l] == sc[r]) {
				l++; r--; 
			} else { 
				int k = r; 
				while (l < k && sc[l] != sc[r]) k--; 
				if (k == l) {
					swap(sc, l, l+1);
					nb_swaps++; 
				} else {
					while (k < r) {
						swap(sc, k, k+1);
						k++; 
						nb_swaps++; 
					}
					l++; r--; 
				}
			}
		}
		return nb_swaps; 
	}

	private static void swap(char[] s, int l, int r) {
		char temp = s[l]; 
		s[l] = s[r]; 
		s[r] = temp; 
		nb_swaps++; 
	}

	private static boolean isJumbledPalindrome(char[] s) { 
		int[] cs = new int[26]; 
		for (char c : s) {
			cs[c - 'a']++; 
		}
		boolean odds = false; 
		for (int i : cs) {
			if (i%2 != 0) {
				if (odds) return false; 
				odds = true; 
			}
		}
		return true;
	}
}