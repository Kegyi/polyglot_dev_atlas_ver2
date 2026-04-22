package stats_test

import (
	"testing"

	"playground/multi_file/internal/stats"
)

func TestSum(t *testing.T) {
	got := stats.Sum([]float64{1, 2, 3})
	if got != 6 {
		t.Errorf("Sum = %v, want 6", got)
	}
}

func TestSumEmpty(t *testing.T) {
	got := stats.Sum(nil)
	if got != 0 {
		t.Errorf("Sum(nil) = %v, want 0", got)
	}
}

func TestAverage(t *testing.T) {
	got := stats.Average([]float64{1, 2, 3})
	if got != 2 {
		t.Errorf("Average = %v, want 2", got)
	}
}

func TestAverageEmpty(t *testing.T) {
	got := stats.Average(nil)
	if got != 0 {
		t.Errorf("Average(nil) = %v, want 0", got)
	}
}

func TestMax(t *testing.T) {
	got := stats.Max([]float64{1, 5, 3, 2})
	if got != 5 {
		t.Errorf("Max = %v, want 5", got)
	}
}

func TestMaxEmpty(t *testing.T) {
	got := stats.Max(nil)
	if got != 0 {
		t.Errorf("Max(nil) = %v, want 0", got)
	}
}
