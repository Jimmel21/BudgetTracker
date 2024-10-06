<!-- src/components/BudgetList.vue -->
<template>
    <div class="budget-list">
      <h2 class="list-title">Budgets</h2>
      <div class="table-container">
        <table class="budget-table">
          <thead>
            <tr>
              <th>Month</th>
              <th>Total Budget ($)</th>
              <th>Total Expenses ($)</th>
              <th>Remaining ($)</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="budget in budgets" :key="budget.id">
              <td>{{ budget.month }}</td>
              <td>{{ formatCurrency(budget.total_budget) }}</td>
              <td>{{ formatCurrency(calculateTotalExpenses(budget.expenses)) }}</td>
              <td>{{ formatCurrency(budget.total_budget - calculateTotalExpenses(budget.expenses)) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['budgets'],
    methods: {
      calculateTotalExpenses(expenses) {
        return expenses.reduce((sum, expense) => sum + expense.amount, 0);
      },
      formatCurrency(value) {
        return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value);
      }
    }
  };
  </script>
  
  <style scoped>
  .budget-list {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .list-title {
    font-size: 1.5rem;
    color: #333;
    margin-bottom: 1.5rem;
    text-align: center;
  }
  
  .table-container {
    overflow-x: auto;
  }
  
  .budget-table {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
  }
  
  .budget-table th,
  .budget-table td {
    padding: 12px;
    border-bottom: 1px solid #e0e0e0;
  }
  
  .budget-table th {
    background-color: #f5f5f5;
    font-weight: bold;
    color: #333;
    text-transform: uppercase;
    font-size: 0.9rem;
  }
  
  .budget-table tr:last-child td {
    border-bottom: none;
  }
  
  .budget-table tr:hover {
    background-color: #f9f9f9;
  }
  
  @media (max-width: 600px) {
    .budget-table {
      font-size: 0.9rem;
    }
  
    .budget-table th,
    .budget-table td {
      padding: 8px;
    }
  }
  </style>