(function (l) {
  "use strict";
  function e() {}
  (e.prototype.respChart = function (e, r, a, o) {
    (Chart.defaults.global.defaultFontColor = "#86889a"),
      (Chart.defaults.scale.gridLines.color = "rgba(108, 120, 151, 0.1)");
    var t = e.get(0).getContext("2d"),
      n = l(e).parent();
    function s() {
      e.attr("width", l(n).width());
      switch (r) {
        case "Bar":
          new Chart(t, { type: "bar", data: a, options: o });
          break;
      }
    }
    l(window).resize(s), s();
  }),
    (e.prototype.init = function () {
      var chart = window.chartData;
      this.respChart(
        l("#bar"),
        "Bar",
        chart,
        {
          responsive: !0,
          scales: {
            xAxes: [
              { barPercentage: 0.8, categoryPercentage: 0.4, display: !0 },
            ],
          },
        }
      );
    }),
    (l.ChartJs = new e()),
    (l.ChartJs.Constructor = e);
})(window.jQuery),
  (function () {
    "use strict";
    window.jQuery.ChartJs.init();
  })();
