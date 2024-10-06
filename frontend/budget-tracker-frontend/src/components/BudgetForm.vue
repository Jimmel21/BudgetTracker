<!-- src/components/BudgetForm.vue -->
<template>
    <div class="max-w-md mx-auto p-6 bg-white shadow-lg rounded-lg border border-gray-200 mt-10">
        <h2 class="text-2xl font-bold text-center text-gray-800 mb-6">Set Monthly Budget</h2>
        <form @submit.prevent="submitBudget">
            <div class="mb-5">
                <label class="block text-gray-700 font-medium mb-1">Month (YYYY-MM)</label>
                <input 
                    v-model="month" 
                    type="month" 
                    class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 transition duration-200" 
                    required 
                />
            </div>
            <div class="mb-5">
                <label class="block text-gray-700 font-medium mb-1">Total Budget ($)</label>
                <input 
                    v-model.number="total_budget" 
                    type="number" 
                    min="0" 
                    class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 transition duration-200" 
                    required 
                />
            </div>
            <button 
                type="submit" 
                class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 rounded-md transition duration-200"
            >
                Save Budget
            </button>
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
                alert(error.response.data.detail || 'Error saving budget');
            }
        },
    },
};
</script>

<style scoped>
/* Style for the form container */
.max-w-md {
    max-width: 400px; /* Limit max width for better readability */
}

.bg-white {
    background-color: #fff; /* Clean white background */
}

.shadow-lg {
    box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
}

.rounded-lg {
    border-radius: 8px; /* Rounded corners for a softer look */
}

.border {
    border: 1px solid #e2e8f0; /* Light border color */
}

.mt-10 {
    margin-top: 2.5rem; /* Space above the form */
}

.text-center {
    text-align: center; /* Center align the header */
}

.mb-1 {
    margin-bottom: 0.25rem; /* Space below the label */
}

.mb-5 {
    margin-bottom: 1.25rem; /* Space below the input fields */
}

/* Style for input fields */
input {
    transition: border-color 0.2s ease-in-out; /* Smooth transition for border */
}

/* Focus effect */
input:focus {
    border-color: #4299e1; /* Border color on focus */
    outline: none; /* Remove default outline */
}

/* Button styling */
button {
    transition: background-color 0.2s ease-in-out; /* Smooth transition for button */
}

/* Hover effect for button */
button:hover {
    background-color: #2b6cb0; /* Darker blue on hover */
}
</style>
