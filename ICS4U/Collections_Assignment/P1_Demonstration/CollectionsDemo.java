import java.util.*;

public class CollectionsDemo {
    public static void main(String[] args) {
        // --- ArrayList ---
        ArrayList<String> names = new ArrayList<String>();
        // add elements
        names.add("Ricky");
        names.add("Aaron");
        names.add("Avi");
        System.out.println("\nArrayList: " + names);
        // get size
        System.out.println("Size: " + names.size());
        // update element
        names.set(2, "Aviare");
        System.out.println("ArrayList Updated: " + names);
        // search element
        if(names.contains("Alex"))
            System.out.println("Found Alex in ArrayList");
        else
            System.out.println("Did not find Alex in ArrayList");
        // sort arraylist
        Collections.sort(names);
        System.out.println("ArrayList Sorted: " + names);
        // remove element
        names.remove("Ricky");
        System.out.println("ArrayList Removed: " + names);
        System.out.println("--------------------\n");
        
        
        // --- LinkedList ---
        LinkedList<Double> numbers = new LinkedList<Double>();
        // add elements
        numbers.add(3.14);
        numbers.add(1.62);
        numbers.add(2.72);
        System.out.println("LinkedList:" + numbers);
        // get size
        System.out.println("Size: " + numbers.size());
        // get reversed linkedList
        Iterator itr = numbers.descendingIterator();
        System.out.print("LinkedList Reversed: [");
        int commaSpacing = numbers.size();
        while(itr.hasNext()) {
            System.out.print(itr.next());
            commaSpacing--;
            if(commaSpacing > 0)
                System.out.print(", ");
        }
        // swap elements
        Collections.swap(numbers, 0, 1);
        System.out.println("]\nLinkedList Swap: " + numbers);
        // join linkedList
        LinkedList<Double> numbers2 = new LinkedList<Double>();
        numbers2.add(0.5);
        numbers2.add(-2.15);
        numbers2.add(8.03);
        numbers.addAll(numbers2);
        System.out.println("LinkedList Merged: " + numbers);
        System.out.println("--------------------\n");


        // --- HashSets ---
        HashSet<Integer> integers = new HashSet<Integer>();
        // add elements
        integers.add(5);
        integers.add(2);
        integers.add(8);
        integers.add(3);
        System.out.println("HashSet: " + integers);
        // get size
        System.out.println("Size: " + integers.size());
        // clone linked list
        HashSet<Integer> integers2 = (HashSet)integers.clone();
        System.out.println("HashSet Cloned: " + integers2);
        // remove
        integers.remove(3);
        System.out.println("HashSet Updated: " + integers);
        // clear hash set
        integers.removeAll(integers);
        System.out.println("HashSet Cleared: " + integers);
        System.out.println("--------------------\n");


        // --- Queues ---
        PriorityQueue<Boolean> values = new PriorityQueue<Boolean>();
        // add elements
        values.add(false);
        values.add(false);
        values.add(true);
        values.add(true);
        System.out.println("Queue: " + values);
        // get size
        System.out.println("Size: " + values.size());
        // get front element of queue
        System.out.println("Front Value: " + values.peek());
        System.out.println("Queue: " + values);
        // remove front element of queue
        values.poll();
        System.out.println("Queue Updated: " + values);
            // you can also get and remove in one step:
        System.out.println("Queue First Element: " + values.poll());
        System.out.println("Queue Updated: " + values);
        // convert queue to array
        List<Boolean> valuesList = new ArrayList<Boolean>(values);
        System.out.println("Array version of Queue: " + valuesList);
        System.out.println("--------------------\n");


        // --- Maps ---
        HashMap<Character, Character> decode = new HashMap<Character, Character>();
        // add key and value to map (this example is a Caesar Cipher)
        for(char c = 'a'; c <= 'z'; c++)
            // each letter maps to the next letter in the alphabet. Note that 'z+1' passes the alphabet and will return the next ASCII value so this can be changed later 
            decode.put(c, (char)(c+1));
        System.out.println("Map: " + decode);
        // replace key-value pair
        decode.replace('z', 'a');
        System.out.println("Map: " + decode);
        // get size
        System.out.println("Size: " + decode.size());
        // get value in map from key
        System.out.println("Value for key of \'d\': " + decode.get('d'));
            // example of practical usage
        String code = "gdkkn";
        System.out.print(code + " processed in the map: ");
        for(int i = 0; i < code.length(); i++)
            System.out.print(decode.get(code.charAt(i)));
        // check if key exists
        if(decode.containsKey('z'))
            System.out.println("\nFound key \'z\'");
        else
            System.out.println("\nDid not find key \'z\'");
        // check if value exists
        if(decode.containsValue('{'))
            System.out.println("Found value \'{\'");
        else
            System.out.println("Did not find value \'{\'");
    }
}