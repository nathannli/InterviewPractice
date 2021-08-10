import java.util.HashMap;

public class CountSums {
    public int count_sums(int[] array, int sums) {
        int count = 0;

        // setup hashset for quick access
        HashMap<Integer, Integer> data = new HashMap<>();
        for (int i = 0; i < array.length; i++) {
            if (!data.containsKey(array[i]))
                data.put(array[i], 0);
        }

        for (int j = 0; j < array.length; j++) {
            int b = sums - array[j];
            if (data.get(array[j]) == 1 || data.get(b) == 1)
                continue;
            else if (data.containsKey(b)) {
                count++;
                data.put(b, 1);
            }
        }

        return count;
    }

    public static void main(String args[]) {
        CountSums cs = new CountSums();
//        int[] the_array = new int[]{1,5,7,-1};
        int[] the_array = new int[]{1,1,5,7,-1,5,5};
        int sums = 6;
        System.out.println(cs.count_sums(the_array, sums));
    }
}
