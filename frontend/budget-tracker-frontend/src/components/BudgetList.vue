<!-- src/components/BudgetList.vue -->
<template>
    <div class="mt-8">
      <h2 class="text-xl font-semibold mb-4">Budgets</h2>
      <table class="min-w-full bg-white">
        <thead>
          <tr>
            <th class="py-2">Month</th>
            <th class="py-2">Total Budget ($)</th>
            <th class="py-2">Total Expenses ($)</th>
            <th class="py-2">Remaining ($)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="budget in budgets" :key="budget.id" class="text-center">
            <td class="py-2">{{ budget.month }}</td>
            <td class="py-2">{{ budget.total_budget }}</td>
            <td class="py-2">{{ calculateTotalExpenses(budget.expenses) }}</td>
            <td class="py-2">{{ budget.total_budget - calculateTotalExpenses(budget.expenses) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    props: ['budgets'],
    methods: {
      calculateTotalExpenses(expenses) {
        return expenses.reduce((sum, expense) => sum + expense.amount, 0).toFixed(2);
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add any component-specific styles here */
  </style>
  