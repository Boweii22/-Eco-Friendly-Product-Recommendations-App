// Pie Chart for Expense Breakdown
const pieCanvas = document.getElementById('expensePieChart').getContext('2d');
const pieData = {
    labels: ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Savings'],
    datasets: [{
        data: [1200, 800, 400, 600, 1000], // Replace with actual data
        backgroundColor: ['#f44336', '#2196f3', '#ffeb3b', '#9c27b0', '#4caf50'],
        hoverBackgroundColor: ['#d32f2f', '#1976d2', '#fbc02d', '#7b1fa2', '#388e3c']
    }]
};

new Chart(pieCanvas, {
    type: 'pie',
    data: pieData
});
