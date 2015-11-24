/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package congtaozailai;

import java.util.*;

public class Searching {

    private static Random rand = new Random(45);
    private static String[] flavors = {
        "kkdkc", "jjlkc"
    };

    public static void main(String[] args) {
        int a = 9, b = 3;
        System.out.println(a % b);

        Random random = new Random(47);
        for (int i = 0; i < 25; i++) {
            double t1 = random.nextGaussian()*100;
            System.out.println(t1);
        }

    }

}
