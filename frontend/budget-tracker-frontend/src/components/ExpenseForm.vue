<!-- src/components/ExpenseForm.vue -->
<template>
    <div class="expense-form">
      <h2 class="form-title">Add New Expense</h2>
      <form @submit.prevent="submitExpense">
        <div class="input-group">
          <select
            v-model="selectedBudgetId"
            required
          >
            <option disabled value="">-- Select a budget --</option>
            <option v-for="budget in budgets" :key="budget.id" :value="budget.id">
              {{ budget.month }} - ${{ budget.total_budget }}
            </option>
          </select>
          <label>Budget</label>
        </div>
  
        <div class="input-group">
          <input
            v-model="category"
            type="text"
            required
            placeholder=" "
          />
          <label>Category</label>
        </div>
  
        <div class="input-group">
          <input
            v-model.number="amount"
            type="number"
            min="0"
            step="0.01"
            required
            placeholder=" "
          />
          <label>Amount ($)</label>
        </div>
  
        <div class="input-group">
          <input
            v-model="date"
            type="date"
            required
          />
          <label>Date</label>
        </div>
  
        <button type="submit">Add Expense</button>
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
        if (!this.validateForm()) return;
  
        const expenseData = {
          category: this.category,
          amount: this.amount,
          date: this.date,
        };
  
        try {
          const response = await axios.post(
            `${API_URL}/expenses/`,
            expenseData,
            {
              params: { budget_id: this.selectedBudgetId },
              headers: { 'Content-Type': 'application/json' },
            }
          );
  
          this.$emit('expense-saved', response.data);
          this.resetForm();
        } catch (error) {
          console.error('Error adding expense:', error);
          alert(error.response?.data?.detail || 'Failed to add expense. Please try again.');
        }
      },
      validateForm() {
        if (!this.selectedBudgetId) {
          alert('Please select a budget.');
          return false;
        }
        if (!this.category.trim()) {
          alert('Please enter a valid category.');
          return false;
        }
        if (this.amount <= 0) {
          alert('Please enter a valid amount.');
          return false;
        }
        if (!this.date) {
          alert('Please select a date.');
          return false;
        }
        return true;
      },
      resetForm() {
        this.selectedBudgetId = '';
        this.category = '';
        this.amount = null;
        this.date = '';
      },
    },
  };
  </script>
  
  <style scoped>
  .expense-form {
    max-width: 400px;
    margin: 2rem auto;
    padding: 2rem;
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .form-title {
    font-size: 1.5rem;
    color: #333;
    margin-bottom: 1.5rem;
    text-align: center;
  }
  
  .input-group {
    position: relative;
    margin-bottom: 1.5rem;
  }
  
  input, select {
    width: 100%;
    padding: 10px 0;
    font-size: 1rem;
    color: #333;
    border: none;
    border-bottom: 1px solid #ddd;
    outline: none;
    background: transparent;
    transition: border-color 0.2s;
  }
  
  input:focus, select:focus {
    border-bottom-color: #3498db;
  }
  
  label {
    position: absolute;
    top: 0;
    left: 0;
    padding: 10px 0;
    font-size: 1rem;
    color: #999;
    pointer-events: none;
    transition: 0.2s ease all;
  }
  
  input:focus ~ label,
  input:not(:placeholder-shown) ~ label,
  select:focus ~ label,
  select:not(:placeholder-shown) ~ label {
    top: -20px;
    font-size: 0.8rem;
    color: #3498db;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.2s;
  }
  
  button:hover {
    background-color: #2980b9;
  }
  
  select {
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    background-image: url('data:image/svg+xml;utf8,<svg fill="black" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/><path d="M0 0h24v24H0z" fill="none"/></svg>');
    background-repeat: no-repeat;
    background-position-x: 100%;
    background-position-y: 5px;
  }
  </style>