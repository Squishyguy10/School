enum SeriesCategory {
    ARITHMETIC,
    GEOMETRIC,
    FIBONACCI,
    FACTORIAL;

    public static void printSeries() {
        for(SeriesCategory series : SeriesCategory.values()) {
            System.out.println(series);
        }
    }

    public static int arithmeticSeries(int start, int diff, int terms) {
        if(terms == 0) {
            return start;
        }
        return arithmeticSeries(start+diff, diff, terms-1);
    }

    public static int geometricSeries(int start, int ratio, int terms) {
        if(terms == 0) {
            return start;
        }
        return geometricSeries(start*ratio, ratio, terms-1);
    }

    public static int fibonacciSeries(int n) {
        if(n == 0) {
            return 0;
        }
        if(n == 1) {
            return 1;
        }
        return fibonacciSeries(n-1) + fibonacciSeries(n-2);
    }

    public static int factorialSeries(int num) {
        if(num <= 1) {
            return 1;
        }
        return num * factorialSeries(num-1);
    }
}