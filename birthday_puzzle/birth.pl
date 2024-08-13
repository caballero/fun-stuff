#!usr/bin/perl
use strict;
use warnings;

my $year = 2021;

for (my $y = $year - 100; $y < $year; $y++) {
    my $age = $year - $y;
    my @dig = split(//, $y);
    my $sum = 0;
    foreach my $d (@dig) {
        $sum += $d;
    }
    if ($sum == $age) {
        print "$y is valid (sum=$sum, age=$age)!\n";
    }
}