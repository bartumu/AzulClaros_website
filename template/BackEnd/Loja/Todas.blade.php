@extends('BackEnd.app')

@section('Conteudo')

<div class="main-content">

    <div class="page-content">
        <div class="container-fluid">

            <!-- start page title -->
            <div class="row">
                <div class="col-12">
                    <div class="page-title-box d-flex align-items-center justify-content-between">
                        <h4 class="mb-0 font-size-18">Todas as Lojas</h4>

                        <div class="page-title-right">
                            <ol class="breadcrumb m-0">
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Azul Claros</a></li>
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Listas</a></li>
                                <li class="breadcrumb-item active">Todas as Lojas</li>
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
                            <p class="card-title-desc">Aqui são apresentados todas as nossas <code>.Lojas</code> e suas
                                <code>&lt;Informações&gt;</code>.
                            </p>
                            <div class="table-responsive">
                                <table class="table mb-0">
                                @php($i=1)
                                    @if (count($Loja)==0) <h2>Não tem Lojas Cadastradas</h2>

                                        @else
                                        <thead>
                                            <tr>
                                                <th>#</th>
                                                <th> Nome</th>
                                                <th>Endereço</th>
                                                <th>Tel</th>
                                                <th>Ações</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            @foreach ($Loja as $loja)

                                            <tr>
                                                <th scope="row">{{$i++}}</th>
                                                <td>{{$loja->nome}}</td>
                                                <td>{{$loja->endereco}}</td>
                                                <td><span>{{$loja->numero}}</span>
                                                </td>
                                                <td><a href="{{Route('Loja.Editar', $loja->id)}}" class="btn btn-outline-secondary btn-sm edit" title="Editar">
                                                        <i class="fas fa-pencil-alt"></i>
                                                    </a>
                                                    |
                                                    <a href="{{Route('Loja.Eliminar', $loja->id)}}" class="btn btn-outline-secondary btn-sm edit" title="Deletar">
                                                        <i class="fas fa-trash-alt"></i>
                                                    </a>
                                                </td>
                                            </tr>
                                            @endforeach
                                            
                                        </tbody>
                                        @endif
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


        @include('BackEnd.layout.footer')
    </div>

    @endsection