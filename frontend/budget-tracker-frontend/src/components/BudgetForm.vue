<!-- src/components/BudgetForm.vue -->
<template>
    <div class="budget-form">
      <h2 class="form-title">Set Monthly Budget</h2>
      <form @submit.prevent="submitBudget">
        <div class="input-group">
          <input
            v-model="month"
            type="month"
            required
          />
          <label>Month (YYYY-MM)</label>
        </div>
        <div class="input-group">
          <input
            v-model.number="total_budget"
            type="number"
            min="0"
            step="0.01"
            required
          />
          <label>Total Budget ($)</label>
        </div>
        <button type="submit">Save Budget</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        month: '',
        total_budget: 0,
      };
    },
    methods: {
      async submitBudget() {
        try {
          const response = await axios.post('http://localhost:8000/budgets/', {
            month: this.month,
            total_budget: this.total_budget,
          });
          this.$emit('budget-saved', response.data);
          this.month = '';
          this.total_budget = 0;
        } catch (error) {
          alert(error.response?.data?.detail || 'Error saving budget');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .budget-form {
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
  
  input {
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
  
  input:focus {
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
  input:not(:placeholder-shown) ~ label {
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
  </style>