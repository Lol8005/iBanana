<?php

$category="CPU";

$products = array(
  new Product("AMD Ryzen 3 3200G", "assets/Product/CPU/cpu1.jpg", "$ 100.81", "Ryzen 3 3200G has 4 MB of L3 cache and operates at 3.6 GHz by default, but can boost up to 4 GHz, depending on the workload."),
  new Product("Intel Core i3-13100F", "assets/Product/CPU/cpu2.jpg", "$ 116.05", "CPU Specifications ; Total Cores. 4 ; # of Performance-cores. 4 ; # of Efficient-cores. 0 ; Total Threads. 8 ; Max Turbo Frequency. 4.50 GHz."),
  new Product("AMD Ryzen 3 3100", "assets/Product/CPU/cpu3.jpg", "$ 120.40", "The AMD Ryzen 3 3100 is a desktop processor with 4 cores, launched in April 2020."),
  new Product("AMD Ryzen 5 5600G", "assets/Product/CPU/cpu4.jpg", "$ 122.59", "The AMD Ryzen 5 5600G is a desktop processor with 6 cores, launched in April 2021."),
  new Product("AMD Ryzen 5 4500", "assets/Product/CPU/cpu5.jpeg", "$ 126.93", "Core Count 6, Integrated Graphics None, Performance Boost Clock Up to 4.1GHz, Performance Core Clock 3.6GHz, Thermal Design Power (TDP) 65W."),
  new Product("Intel Core i3-13100", "assets/Product/CPU/cpu6.jpg", "$ 133.46", "CPU Specifications ; Total Cores. 4 ; # of Performance-cores. 4 ; # of Efficient-cores. 0 ; Total Threads. 8 ; Max Turbo Frequency. 4.50 GHz."),
);

include 'productCarousel.php';
?>