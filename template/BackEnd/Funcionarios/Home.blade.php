@extends('BackEnd.app')

@section('Conteudo')
<div class="main-content">

    <div class="page-content">
        <div class="container-fluid">

            <!-- start page title -->
            <div class="row">
                <div class="col-12">
                    <div class="page-title-box d-flex align-items-center justify-content-between">
                        <h4 class="mb-0 font-size-18">Todas os Pedidos</h4>

                        <div class="page-title-right">
                            <ol class="breadcrumb m-0">
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Azul Claros</a></li>
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Listas</a></li>
                                <li class="breadcrumb-item active">Todos os Pedidos</li>
                            </ol>
                        </div>

                    </div>
                </div>
            </div>
            <!-- end page title -->

            <div class="row">
                <div class="col-md-12 col-xl-12">
                    <div class="card">
                        <div class="card-body">

                            <h5 class="card-title"></h5>
                            <p class="card-title-desc">Aqui são apresentados todos as Pedidos da <code>.Lojas</code> e suas
                                <code>&lt;Informações&gt;</code>.
                            </p>
                            <div class="table-responsive">
                                <table class="table mb-0">
                                 <!--    @if (count($Func)==0)
                                    <h2>Não Tem Nenhum Funcionário Cadastrado Ainda!</h2>
                                    @else
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th> Nome</th>
                                            <th>Genero</th>
                                            <th>Loja</th>
                                            <th>Ações</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        @php($i=1)
                                        @foreach ($Func as $func)
                                        <tr>
                                            <th scope="row">{{$i++}}</th>
                                            <td>{{$func->nome}}</td>
                                            <td>{{$func->genero}}</td>
                                            <td><span>{{$func->loja}}</span>
                                            </td>
                                            <td><a href="{{Route('Func.Editar', $func->id)}}" class="btn btn-outline-secondary btn-sm edit" title="Editar">
                                                    <i class="fas fa-pencil-alt"></i>
                                                </a>
                                                |
                                                <a href="{{Route('Func.Eliminar', $func->id)}}" class="btn btn-outline-secondary btn-sm edit" title="Deletar">
                                                    <i class="fas fa-trash-alt"></i>
                                                </a>
                                            </td>
                                        </tr>
                                        @endforeach
                                    </tbody>
                                    @endif -->
                                </table>
                                <!-- end table -->
                            </div>
                        </div>
                    </div>
                </div>
                <!-- end col -->


            </div>
            <!-- end row -->



            <!-- container-fluid -->
        </div>
        <!-- End Page-content -->
    </div>
    @include('BackEnd.layout.footer')
</div>
@endsection