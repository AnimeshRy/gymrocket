// Member Chart

async function memChart() {
  try {
    const response = await fetch('memberchart/');
    const val = await response.json();
    return val;
  } catch (error) {
    return 'Error Getting Data';
  }
}

memChart().then((data) => {
  if (data === 'Error Getting Data') {
    let div = document.getElementById('memChartDiv');
    div.classList.add('hidden');
  }
  new Chart(document.getElementById('chartjs-7'), {
    type: 'bar',
    data: {
      labels: data.labels,
      datasets: [
        {
          label: 'Monthly Members',
          data: data.data,
          borderColor: 'rgb(255, 99, 132)',
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
        },
      ],
    },
    options: {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
            },
          },
        ],
      },
    },
  });
});

// Payment Chart
async function payChart() {
  try {
    const response = await fetch('paymentchart/');
    const val = await response.json();
    return val;
  } catch (error) {
    return 'Error Getting Data';
  }
}

payChart().then((data) => {
  if (data === 'Error Getting Data') {
    let div = document.getElementById('paychartDiv');
    div.classList.add('hidden');
  }

  new Chart(document.getElementById('chartjs-0'), {
    type: 'line',
    data: {
      labels: data.labels,
      datasets: [
        {
          label: '₹ Rupees',
          data: data.data,
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          lineTension: 0.1,
        },
      ],
    },
    options: {},
  });
});

let DashboardAnchor = document.getElementById('dashboard-a');
let MobileDashboardAnchor = document.getElementById('dashboard-mobile');
DashboardAnchor.classList.add('bg-gray-900', 'text-white');
MobileDashboardAnchor.classList.add('bg-gray-900', 'text-white');
