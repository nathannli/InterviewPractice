import java.util.ArrayList;
import java.util.HashSet;

public class CountSums {
    public int count_sums(int[] array, int sums) {
        int count = 0;

        // setup hashset for quick access
        HashSet<Integer> data = new HashSet<>();
        for (int i = 0; i < array.length; i++) {
            data.add(array[i]);
        }

        ArrayList<Integer> seen = new ArrayList<>();
        for (int j = 0; j < array.length; j++) {
            int b = sums - array[j];
            if (seen.contains(array[j]))
                continue;
            if (data.contains(b)) {
                count++;
                seen.add(b);
            }

        }

        return count;
    }

    public static void main(String args[]) {
        CountSums cs = new CountSums();
//        int[] the_array = new int[]{1,5,7,-1};
        int[] the_array = new int[]{1,5,7,-1,5};
        int sums = 6;
        System.out.println(cs.count_sums(the_array, sums));
    }
}
