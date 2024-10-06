<!-- src/components/BudgetChart.vue -->
<template>
    <div class="budget-chart">
      <h2 class="chart-title">Expenses Chart</h2>
      <div v-if="chartDataReady" class="chart-container">
        <bar-chart :chart-data="chartData" :options="chartOptions"></bar-chart>
      </div>
      <p v-else class="loading-text">Loading chart data...</p>
    </div>
  </template>
  
  <script>
  import { Bar } from 'vue-chartjs';
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);
  
  export default {
    components: {
      BarChart: Bar
    },
    props: {
      budgets: {
        type: Array,
        required: true
      }
    },
    data() {
      return {
        chartDataReady: false
      };
    },
    computed: {
      chartData() {
        if (!this.budgets || this.budgets.length === 0) {
          return {
            labels: [],
            datasets: []
          };
        }
        
        const labels = this.budgets.map(b => b.month);
        const expenses = this.budgets.map(b => {
          return Array.isArray(b.expenses)
            ? b.expenses.reduce((sum, expense) => sum + expense.amount, 0)
            : 0;
        });
        
        return {
          labels,
          datasets: [
            {
              label: 'Total Expenses',
              backgroundColor: '#42b883',
              data: expenses
            }
          ]
        };
      },
      chartOptions() {
        return {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: true,
              position: 'top',
            },
            title: {
              display: true,
              text: 'Monthly Expenses',
              font: {
                size: 16,
                weight: 'bold',
              },
            },
          },
          scales: {
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: 'Amount ($)',
              },
            },
            x: {
              title: {
                display: true,
                text: 'Month',
              },
            },
          },
        };
      }
    },
    watch: {
      budgets: {
        handler(newBudgets) {
          this.chartDataReady = newBudgets && newBudgets.length > 0;
        },
        immediate: true
      }
    }
  };
  </script>
  
  <style scoped>
  .budget-chart {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .chart-title {
    font-size: 1.5rem;
    color: #333;
    margin-bottom: 1.5rem;
    text-align: center;
  }
  
  .chart-container {
    position: relative;
    height: 400px;
    margin-top: 1rem;
  }
  
  .loading-text {
    text-align: center;
    color: #666;
    font-style: italic;
  }
  </style>