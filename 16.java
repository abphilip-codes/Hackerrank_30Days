// https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        String S = in.nextLine();
        try{
            int allen = Integer.parseInt(S);
            System.out.println(allen);
        }
        catch(NumberFormatException exp){
            System.out.println("Bad String");
        }
        in.close();
    }
}