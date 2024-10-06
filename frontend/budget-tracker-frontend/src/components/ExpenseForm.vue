<!-- src/components/ExpenseForm.vue -->
<template>
    <div class="max-w-md mx-auto p-4 bg-white shadow-md rounded mt-6">
      <h2 class="text-xl font-semibold mb-4">Add New Expense</h2>
      <form @submit.prevent="submitExpense">
        <!-- Budget Selection -->
        <div class="mb-4">
          <label class="block text-gray-700 mb-2" for="budget">Select Budget</label>
          <select
            v-model="selectedBudgetId"
            id="budget"
            class="w-full px-3 py-2 border rounded"
            required
          >
            <option disabled value="">-- Please select a budget --</option>
            <option v-for="budget in budgets" :key="budget.id" :value="budget.id">
              {{ budget.month }} - ${{ budget.total_budget }}
            </option>
          </select>
        </div>
  
        <!-- Category Input -->
        <div class="mb-4">
          <label class="block text-gray-700 mb-2" for="category">Category</label>
          <input
            v-model="category"
            type="text"
            id="category"
            placeholder="e.g., Groceries"
            class="w-full px-3 py-2 border rounded"
            required
          />
        </div>
  
        <!-- Amount Input -->
        <div class="mb-4">
          <label class="block text-gray-700 mb-2" for="amount">Amount ($)</label>
          <input
            v-model.number="amount"
            type="number"
            id="amount"
            min="0"
            step="0.01"
            placeholder="e.g., 50.75"
            class="w-full px-3 py-2 border rounded"
            required
          />
        </div>
  
        <!-- Date Input -->
        <div class="mb-4">
          <label class="block text-gray-700 mb-2" for="date">Date</label>
          <input
            v-model="date"
            type="date"
            id="date"
            class="w-full px-3 py-2 border rounded"
            required
          />
        </div>
  
        <!-- Submit Button -->
        <button
          type="submit"
          class="w-full bg-green-500 text-white py-2 rounded hover:bg-green-600 transition-colors"
        >
          Add Expense
        </button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { API_URL } from '../config';
  
  export default {
    name: 'ExpenseForm',
    props: {
      budgets: {
        type: Array,
        required: true,
        default: () => [],
      },
    },
    data() {
      return {
        selectedBudgetId: '',
        category: '',
        amount: null,
        date: '',
      };
    },
    methods: {
      async submitExpense() {
        // Basic Validation
        if (!this.selectedBudgetId) {
          alert('Please select a budget.');
          return;
        }
        if (!this.category.trim()) {
          alert('Please enter a valid category.');
          return;
        }
        if (this.amount <= 0) {
          alert('Please enter a valid amount.');
          return;
        }
        if (!this.date) {
          alert('Please select a date.');
          return;
        }
  
        // Prepare Expense Data
        const expenseData = {
          category: this.category,
          amount: this.amount,
          date: this.date,
        };
  
        try {
          // Make POST request to add expense
          const response = await axios.post(
            `${API_URL}/expenses/`,
            expenseData,
            {
              params: { budget_id: this.selectedBudgetId },
              headers: {
                'Content-Type': 'application/json',
              },
            }
          );
  
          // Emit the new expense to the parent component
          this.$emit('expense-saved', response.data);
  
          // Reset Form Fields
          this.selectedBudgetId = '';
          this.category = '';
          this.amount = null;
          this.date = '';
        } catch (error) {
          console.error('Error adding expense:', error);
          const errorMessage =
            error.response?.data?.detail || 'Failed to add expense. Please try again.';
          alert(errorMessage);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Optional: Add any component-specific styles here */
  </style>
  