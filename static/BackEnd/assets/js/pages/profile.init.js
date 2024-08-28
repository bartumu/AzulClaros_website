var config = {
  type: "line",
  data: {
    labels: [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "Augest",
      "September",
    ],
    datasets: [
      {
        label: "Conversion Rate",
        fill: !1,
        backgroundColor: "#4eb7eb",
        borderColor: "#4eb7eb",
        data: [44, 60, -33, 58, -4, 57, -89, 60, -33, 58, -22, 35],
      },
      {
        label: "Average Sale Value",
        fill: !1,
        backgroundColor: "#e3eaef",
        borderColor: "#e3eaef",
        borderDash: [5, 5],
        data: [-68, 41, 86, -49, 2, 65, -64, 86, -49, 2, -8, 41],
      },
    ],
  },
  options: {
    responsive: !0,
    tooltips: { mode: "index", intersect: !1 },
    hover: { mode: "nearest", intersect: !0 },
    legend: { labels: { fontColor: "#86889a" } },
    scales: {
      xAxes: [
        {
          display: !0,
          gridLines: { color: "rgba(0,0,0,0.1)" },
          ticks: { fontColor: "#86889a" },
        },
      ],
      yAxes: [
        {
          gridLines: { color: "rgba(255,255,255,0.05)", fontColor: "#fff" },
          ticks: { max: 100, min: -100, stepSize: 20, fontColor: "#86889a" },
        },
      ],
    },
  },
};
(window.onload = function () {
  
  window.myLine = new Chart(e, config);
}),
  $(".mfp-image").magnificPopup({
    type: "image",
    mainClass: "mfp-with-zoom",
    gallery: { enabled: !0, navigateByImgClick: !0, preload: [0, 1] },
  }),
  $(".dropify").dropify();
