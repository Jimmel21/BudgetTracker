<!-- src/App.vue -->
<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Header Section -->
    <header class="bg-blue-600 text-white p-4 shadow">
      <div class="container mx-auto">
        <h1 class="text-2xl font-bold">Monthly Budget Tracker</h1>
      </div>
    </header>

    <!-- Main Content -->
    <main class="container mx-auto p-4">
      <!-- Budget Form Component -->
      <BudgetForm @budget-saved="handleBudgetSaved" />

      <!-- Expense Form Component -->
      <ExpenseForm :budgets="budgets" @expense-saved="handleExpenseSaved" />

      <!-- Budget List Component -->
      <BudgetList :budgets="budgets" />

      <!-- Budget Chart Component -->
      <BudgetChart :budgets="budgets" />
    </main>

    <!-- Footer Section -->
    <footer class="bg-blue-600 text-white p-4 mt-8">
      <div class="container mx-auto text-center">
        &copy; 2024 Budget Tracker. All rights reserved.
      </div>
    </footer>
  </div>
</template>

<script>
import axios from 'axios';
import BudgetForm from './components/BudgetForm.vue';
import ExpenseForm from './components/ExpenseForm.vue';
import BudgetList from './components/BudgetList.vue';
import BudgetChart from './components/BudgetChart.vue';
import { API_URL } from './config';

export default {
  name: 'App',
  components: {
    BudgetForm,
    ExpenseForm,
    BudgetList,
    BudgetChart
  },
  data() {
    return {
      budgets: []
    };
  },
  methods: {
    // Fetch all budgets from the backend
    async fetchBudgets() {
      try {
        const response = await axios.get(`${API_URL}/budgets/`);
        this.budgets = response.data;
      } catch (error) {
        console.error("Error fetching budgets:", error);
        alert("Failed to load budgets. Please try again later.");
      }
    },
    // Handle event when a new budget is saved
    handleBudgetSaved(newBudget) {
      this.budgets.push(newBudget);
    },
    // Handle event when a new expense is saved
    handleExpenseSaved(newExpense) {
      // Find the corresponding budget and add the expense
      const budget = this.budgets.find(b => b.id === newExpense.budget_id);
      if (budget) {
        budget.expenses.push(newExpense);
      }
    }
  },
  mounted() {
    this.fetchBudgets();
  }
};
</script>

<style>
/* Optional: Global styles can be added here */
body {
  font-family: 'Inter', sans-serif;
}
</style>
