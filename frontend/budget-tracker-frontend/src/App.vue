<!-- src/App.vue -->
<template>
  <div class="app-container">
    <!-- Header Section -->
    <header class="app-header">
      <div class="header-content">
        <h1 class="app-title">
          <span class="title-icon">💰</span>
          Budget<span class="title-accent">Master</span>
        </h1>
        <p class="app-subtitle">Your Personal Finance Companion</p>
      </div>
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <div class="content-wrapper">
        <!-- Budget Form Component -->
        <section class="app-section">
          <BudgetForm @budget-saved="handleBudgetSaved" />
        </section>

        <!-- Expense Form Component -->
        <section class="app-section">
          <ExpenseForm :budgets="budgets" @expense-saved="handleExpenseSaved" />
        </section>

        <!-- Budget List Component -->
        <section class="app-section">
          <BudgetList :budgets="budgets" />
        </section>

        <!-- Budget Chart Component -->
        <section class="app-section">
          <BudgetChart :budgets="budgets" />
        </section>
      </div>
    </main>

    <!-- Footer Section -->
    <footer class="app-footer">
      <div class="footer-content">
        <p>&copy; {{ new Date().getFullYear() }} BudgetMaster. All rights reserved.</p>
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
    async fetchBudgets() {
      try {
        const response = await axios.get(`${API_URL}/budgets/`);
        this.budgets = response.data;
      } catch (error) {
        console.error("Error fetching budgets:", error);
        alert("Failed to load budgets. Please try again later.");
      }
    },
    handleBudgetSaved(newBudget) {
      this.budgets.push(newBudget);
    },
    handleExpenseSaved(newExpense) {
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
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

body {
  font-family: 'Poppins', sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f0f4f8;
  color: #333;
}

.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.app-header {
  background: linear-gradient(135deg, #3498db, #8e44ad);
  color: white;
  padding: 2rem 0;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.app-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0;
}

.title-icon {
  margin-right: 0.5rem;
}

.title-accent {
  color: #ffd700;
}

.app-subtitle {
  font-size: 1.2rem;
  font-weight: 300;
  margin-top: 0.5rem;
}

.main-content {
  flex-grow: 1;
  padding: 2rem 0;
}

.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.app-section {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
  padding: 1.5rem;
}

.app-footer {
  background-color: #2c3e50;
  color: white;
  padding: 1rem 0;
  text-align: center;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

@media (max-width: 768px) {
  .app-title {
    font-size: 2rem;
  }

  .app-subtitle {
    font-size: 1rem;
  }

  .content-wrapper {
    padding: 0 1rem;
  }
}
</style>