<!-- src/components/BudgetChart.vue -->
<template>
    <div class="mt-8">
      <h2 class="text-xl font-semibold mb-4">Expenses Chart</h2>
      <div v-if="chartDataReady" class="chart-container">
        <bar-chart :chart-data="chartData" :options="chartOptions"></bar-chart>
      </div>
      <p v-else>Loading chart data...</p>
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
          maintainAspectRatio: false
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
  .chart-container {
    position: relative;
    height: 400px;
  }
  </style>