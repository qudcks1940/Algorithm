
import java.util.*;
import java.io.*;
public class Main {
    static int[] arr;
    static int[] list;
    static int[] record;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        arr = new int[N];
        list = new int[N];
        record = new int[N];


        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int j = 0;
        list[j] = arr[0];
        record[0] = 0;
        for (int i = 1; i < N; i++) {
            if (list[j] < arr[i]) {
                list[j + 1] = arr[i];
                record[i] = j + 1;
                j++;
            } else {
                int pos = bs(0, j, arr[i]);
                list[pos] = arr[i];
                record[i] = pos;
            }
        }
        System.out.println(j + 1);

        int idx = j;
        List<Integer> result = new ArrayList<>();
        for(int i = N - 1; i >= 0; i --){
            if(record[i] == idx){
                result.add(arr[i]);
                idx--;
            }
        }
        Collections.sort(result);
        for(int i = 0; i < result.size(); i++){
            System.out.print(result.get(i) + " ");
        }
        br.close();
    }

    static int bs(int l, int r, int v) {
        int m;
        while (l < r) {
            m = (l + r) / 2;
            if (list[m] < v) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return r;
    }
}
