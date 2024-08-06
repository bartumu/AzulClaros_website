/* {% comment %} Tratar do Botão de Levantar {% endcomment %} */
      document.addEventListener('DOMContentLoaded', function() {
        var CliModal = document.getElementById('sairCliModal');
        var FormCli = document.getElementById('FormLevantar');
        $("#tabela tbody").on("click", "#LevantarButton", function(e){
          var $this = $(this);
          $("#FormLevantar").attr("action", $this.attr('href'));
        });
        
        CliModal.addEventListener('show.bs.modal', function(event) {
          
          var button = event.relatedTarget; // Botão que acionou o modal
          
          // Extraia as informações dos atributos de dados
          var codigo = button.getAttribute('data-codigo');
          var nome = button.getAttribute('data-nome');
          var data_reserva = button.getAttribute('data-data_reserva');
          var data_saida = button.getAttribute('data-data_saida');
          var total = button.getAttribute('data-total');
          var estado = button.getAttribute('data-estado');
          
          // Atualize os elementos do modal com os dados do cliente
          var modalTitle = CliModal.querySelector('.modal-title');
          var modalBodyInputCodigo = CliModal.querySelector('.modal-body #codigo_reserva');
          var modalBodyInputNome = CliModal.querySelector('.modal-body #cliente_nome');
          var modalBodyInputDataReserva = CliModal.querySelector('.modal-body #data_reserva');
          var modalBodyInputDataEntrada = CliModal.querySelector('.modal-body #data_saida');
          var modalBodyInputEstado = CliModal.querySelector('.modal-body #estado'); 
          var modalBodyInputTotal = CliModal.querySelector('.modal-body #total');
          
          modalTitle.textContent = 'Detalhes do Cliente ' + codigo;
          modalBodyInputCodigo.textContent = codigo;
          modalBodyInputNome.textContent = nome;
          modalBodyInputDataReserva.textContent = data_reserva;
          modalBodyInputDataEntrada.textContent = data_saida;
          modalBodyInputTotal.textContent = total;
          if (estado == 1){
            modalBodyInputEstado.textContent = 'PAGO';
          }

          $("#FormLevantar").on("submit", function(e){
            let $this = $(this);
            let data = $this.serialize()
          });

          
        });
      });
/* 
      {% comment %} Tratar do Botão de Atender {% endcomment %} */
      document.addEventListener('DOMContentLoaded', function() {
        var CliModal = document.getElementById('atenderCliModal');
        var FormCli = document.getElementById('FormAtender');
        var metodoPagamentoSelect = document.getElementById('metodo-pagamento');
        var ref = document.getElementById('divRef');
        var pag = document.getElementById('divPag');

        $("#tabela tbody").on("click", "#AtenderButton", function(e){
          var $this = $(this);
          $("#FormAtender").attr("action", $this.attr('href'));
        });
        
        CliModal.addEventListener('show.bs.modal', function(event) {
          
          var button = event.relatedTarget; // Botão que acionou o modal
          
          // Extraia as informações dos atributos de dados
          var codigo = button.getAttribute('data-codigo');
          var nome = button.getAttribute('data-nome');
          var data_reserva = button.getAttribute('data-data_reserva');
          var data_entrada = button.getAttribute('data-data_entrada');
          var total = button.getAttribute('data-total');
          
          // Atualize os elementos do modal com os dados do cliente
          var modalTitle = CliModal.querySelector('.modal-title');
          var modalBodyInputCodigo = CliModal.querySelector('.modal-body #codigo_reserva');
          var modalBodyInputNome = CliModal.querySelector('.modal-body #cliente_nome');
          var modalBodyInputDataReserva = CliModal.querySelector('.modal-body #data_reserva');
          var modalBodyInputDataEntrada = CliModal.querySelector('.modal-body #data_entrada');
          var modalBodyInputTotal = CliModal.querySelector('.modal-body #total');
          var modalBodyInputTotalPag = CliModal.querySelector('.modal-body #totalPagamento');
          var modalBodyInputRef = CliModal.querySelector('.modal-body #ref');
          
          modalTitle.textContent = 'Detalhes da Reserva ' + codigo;
          modalBodyInputCodigo.textContent = codigo;
          modalBodyInputNome.textContent = nome;
          modalBodyInputDataReserva.textContent = data_reserva;
          modalBodyInputDataEntrada.textContent = data_entrada;
          modalBodyInputTotal.textContent = total + ' Kz';
          modalBodyInputTotalPag.textContent = total ? total + ' KZ' : 0;
          modalBodyInputRef.textContent = '1234567890';

          //Tratar do Pagamento
          function toggleFields() {
            var selectedMetodo = metodoPagamentoSelect.options[metodoPagamentoSelect.selectedIndex].text;
            if (selectedMetodo === 'Cartão') {
                ref.style.display = 'block';
                pag.style.display = 'none';
            } else if(selectedMetodo === 'Dinheiro') {
                ref.style.display = 'none';
                pag.style.display = 'block';
            }else{
                ref.style.display = 'none';
                pag.style.display = 'none';
            }
        }

        metodoPagamentoSelect.addEventListener('change', toggleFields);
        toggleFields(); // Chamada inicial
        });

        $("#FormAtender").on("submit", function(e){
          let $this = $(this);
          let data = $this.serialize()
          /*$.ajax({
            url: $this.attr("action"),
            type: "POST",
            data: data,
          });*/
        });
      });