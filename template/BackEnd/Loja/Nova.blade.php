@extends('BackEnd.app')

@section('Conteudo')

<div class="main-content">

    @if ($Add==false)

    <!-- EDITAR -->
    <div class="page-content">
        <div class="container-fluid">

            <!-- start page title -->
            <div class="row">
                <div class="col-12">
                    <div class="page-title-box d-flex align-items-center justify-content-between">
                        <h4 class="mb-0 font-size-18">Editar Nova Loja</h4>

                        <div class="page-title-right">
                            <ol class="breadcrumb m-0">
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Azul Claros</a></li>
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Forms</a></li>
                                <li class="breadcrumb-item active">Edição</li>
                            </ol>
                        </div>

                    </div>
                </div>
            </div>
            <!-- end page title -->


            <!-- end row -->

            <div class="row">
                <div class="col-md-12 col-xl-6">
                    <div class="card">
                        <div class="card-body">

                            <form class="custom-validation" action="{{Route('Loja.Actualizar')}}" method="post">
                                @csrf
                                <div class="row gx-3">
                                    <div class="col-md-6">
                                        <div class="mb-3">
                                            <label class="form-label">Nome</label>
                                            <input type="text" class="form-control" name="nome" value="{{$Lojas->nome}}" required placeholder="Nome da Loja" />
                                            <input type="hidden" class="form-control" name="id" value="{{$Lojas->id}}" required placeholder="Nome da Loja" />
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="mb-3">
                                            <label class="form-label">Número</label>
                                            <input type="text" name="numero" value="{{$Lojas->numero}}" class="form-control" required placeholder="Nº de Tel" />
                                        </div>
                                    </div>
                                </div>

                                <div class="mb-3">
                                    <label class="form-label">Endereço</label>
                                    <input type="text" name="endereco" value="{{$Lojas->endereco}}" class="form-control" required placeholder="" />
                                </div>

                                <div class="mb-0">
                                    <div>
                                        <button type="submit" class="btn btn-light waves-effect waves-light">
                                            Editar
                                        </button>
                                        <button type="reset" class="btn btn-danger waves-effect ms-1">
                                            Cancelar
                                        </button>
                                    </div>
                                </div>
                            </form>
                            <!-- end form -->
                        </div>
                        <!-- end cardbody -->
                    </div>
                </div>
                <!-- end col -->

                <!-- end col -->
            </div>
            <!-- end row -->
        </div>
        <!-- container-fluid -->
    </div>
    <!-- FIM EDITAR -->

    @else
    <div class="page-content">
        <div class="container-fluid">

            <!-- start page title -->
            <div class="row">
                <div class="col-12">
                    <div class="page-title-box d-flex align-items-center justify-content-between">
                        <h4 class="mb-0 font-size-18">Adiciona Nova Loja</h4>

                        <div class="page-title-right">
                            <ol class="breadcrumb m-0">
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Azul Claros</a></li>
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Forms</a></li>
                                <li class="breadcrumb-item active">Adicionar</li>
                            </ol>
                        </div>

                    </div>
                </div>
            </div>
            <!-- end page title -->


            <!-- end row -->

            <div class="row">
                <div class="col-md-12 col-xl-6">
                    <div class="card">
                        <div class="card-body">

                            <form class="custom-validation" action="{{Route('Loja.Add')}}" method="post">
                                @csrf
                                <div class="row gx-3">
                                    <div class="col-md-6">
                                        <div class="mb-3">
                                            <label class="form-label">Nome</label>
                                            <input type="text" class="form-control" name="nome" required placeholder="Nome da Loja" />
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="mb-3">
                                            <label class="form-label">Número</label>
                                            <input type="text" name="numero" class="form-control" required placeholder="Nº de Tel" />
                                        </div>
                                    </div>
                                </div>

                                <div class="mb-3">
                                    <label class="form-label">Endereço</label>
                                    <input type="text" name="endereco" class="form-control" required placeholder="" />
                                </div>

                                <div class="mb-0">
                                    <div>
                                        <button type="submit" class="btn btn-light waves-effect waves-light">
                                            Adicionar
                                        </button>
                                        <button type="reset" class="btn btn-danger waves-effect ms-1">
                                            Cancelar
                                        </button>
                                    </div>
                                </div>
                            </form>
                            <!-- end form -->
                        </div>
                        <!-- end cardbody -->
                    </div>
                </div>
                <!-- end col -->

                <!-- end col -->
            </div>
            <!-- end row -->
        </div>
        <!-- container-fluid -->
    </div>
    @endif

    <!-- End Page-content -->


    @include('BackEnd.layout.footer')
</div>

@endsection