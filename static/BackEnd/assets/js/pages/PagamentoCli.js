document.addEventListener('DOMContentLoaded', function() {

    var ref = document.getElementById('divRefCli');
    var pag = document.getElementById('divPagCli');
    var metodoPagamentoSelect = document.getElementById('metodo-pagamento');
    var TotalPag = document.getElementById('TotalPagamento_Cli');
    var ReferenciaBancaria = document.getElementById('referenciaBancaria');

    ReferenciaBancaria.textContent = '123456789';

    function toggleFields() {
        var selectedMetodo = metodoPagamentoSelect.options[metodoPagamentoSelect.selectedIndex].text;
        ref.style.display = selectedMetodo === 'Cartão' ? 'block' : 'none';
        pag.style.display = selectedMetodo === 'Dinheiro' ? 'block' : 'none';
      }

    metodoPagamentoSelect.addEventListener('change', toggleFields);
    toggleFields(); // Chamada inicial
    

})