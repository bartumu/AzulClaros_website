@extends('BackEnd.app')

@section('Conteudo')

<div class="main-content">

    <div class="page-content">
        <div class="container-fluid">
            @if ($Add==false)

            <!-- EDITAR -->
            <!-- start page title -->
            <div class="row">
                <div class="col-12">
                    <div class="page-title-box d-flex align-items-center justify-content-between">
                        <h4 class="mb-0 font-size-18">Editar Novo Funcionário</h4>

                        <div class="page-title-right">
                            <ol class="breadcrumb m-0">
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Azul Claros</a></li>
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Forms</a></li>
                                <li class="breadcrumb-item active">Editar</li>
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

                            <form class="custom-validation" action="{{Route('Func.Actualizar')}}" method="post" enctype="multipart/form-data">
                                @csrf
                                <div class="row gx-3">
                                    <div class="col-md-6">
                                        <div class="mb-3">
                                            <label class="form-label">Nome</label>
                                            <input type="text" name="nome" value="{{$func->nome}}" class="form-control" required placeholder="Nome do Funcionário" />
                                            <input type="hidden" name="id" value="{{$func->id}}" class="form-control" required placeholder="Nome do Funcionário" />
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="mb-0 row">
                                            <label for="example-date-input" class="col-sm-5 form-label">Nascido em:</label>
                                            <div class="col-sm-10">
                                                <input class="form-control" type="date" value="{{$func->dataNasc}}" name="dataNasc" value="Ano-Mes-Dia" id="example-date-input">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="row gx-3">
                                    <div class="col-md-3">
                                        <div class="mb-3">
                                            <select class="form-select" required="" value="{{$func->genero}}" name="genero" aria-label="select example">
                                                <option value="">Genero</option>
                                                <option value="M">M</option>
                                                <option value="F">F</option>
                                            </select>
                                            <div class="invalid-feedback">Example invalid select feedback</div>
                                        </div>
                                    </div>
                                    <div class="col-md-3">

                                        <div class="mb-3">
                                            <div class="mb-3">
                                                <input type="text" name="numero" value="{{$func->numero}}" class="form-control" required placeholder="Nº de Tel" />
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-5">
                                        <div class="mb-3">
                                            <select class="form-select" name="idLoja" value="{{$func->idLoja}}" required="" aria-label="select example">
                                                <option value="">Selecciona a Loja</option>
                                                @foreach ($Lojas as $loja)
                                                <option value="{{$loja->id}}">{{$loja->nome}}</option>
                                                @endforeach
                                            </select>
                                            <div class="invalid-feedback">Example invalid select feedback</div>

                                        </div>
                                    </div>
                                </div>
                                <!-- <div class="row gx-3">
                                    <div class="col-md-11">
                                        <div class="mb-3">
                                            <select class="form-select" required="" aria-label="select example">
                                                <option value="">Selecciona a Loja</option>
                                                <option value="1">One</option>
                                                <option value="2">Two</option>
                                                <option value="3">Three</option>
                                            </select>
                                            <div class="invalid-feedback">Example invalid select feedback</div>

                                        </div>
                                    </div>
                                </div> -->
                                <div class="col-md-11">
                                    <div class="mb-3">
                                        <label class="form-label">Endereço</label>
                                        <input type="text" name="endereco" value="{{$func->endereco}}" class="form-control" required placeholder="Nome do Funcionário" />
                                        <!-- <input type="hidden" name="password" class="form-control" value="azul@claros2024" /> -->
                                    </div>
                                </div>
                                <div class="col-xl-11">
                                    <div class="card">
                                        <div class="card-body">
                                            <h5 class="card-title">Upload de Imagem</h5>
                                            <input type="file" id="input-file-now-custom-1" name="img" class="dropify" data-default-file="{{ (!empty($func->img)) ? url($func->img) : '' }}" />
                                        </div>
                                    </div>
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
            <!-- FIM EDITAR -->
            @else
            <!-- start page title -->
            <div class="row">
                <div class="col-12">
                    <div class="page-title-box d-flex align-items-center justify-content-between">
                        <h4 class="mb-0 font-size-18">Adiciona Novo Funcionário</h4>

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

                            <form class="custom-validation" action="{{Route('Func.Add')}}" method="post" enctype="multipart/form-data">
                                @csrf
                                <div class="row gx-3">
                                    <div class="col-md-6">
                                        <div class="mb-3">
                                            <label class="form-label">Nome</label>
                                            <input type="text" name="nome" class="form-control" required placeholder="Nome do Funcionário" />
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="mb-0 row">
                                            <label for="example-date-input" class="col-sm-5 form-label">Nascido em:</label>
                                            <div class="col-sm-10">
                                                <input class="form-control" type="date" name="dataNasc" value="Ano-Mes-Dia" id="example-date-input">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="row gx-3">
                                    <div class="col-md-3">
                                        <div class="mb-3">
                                            <select class="form-select" required="" name="genero" aria-label="select example">
                                                <option value="">Genero</option>
                                                <option value="M">M</option>
                                                <option value="F">F</option>
                                            </select>
                                            <div class="invalid-feedback">Example invalid select feedback</div>
                                        </div>
                                    </div>
                                    <div class="col-md-3">

                                        <div class="mb-3">
                                            <div class="mb-3">
                                                <input type="text" name="numero" class="form-control" required placeholder="Nº de Tel" />
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-5">
                                        <div class="mb-3">
                                            <select class="form-select" name="idLoja" required="" aria-label="select example">
                                                <option value="">Selecciona a Loja</option>
                                                @forelse ($Lojas as $loja)
                                                <option value="{{$loja->id}}" {{old('idLoja') == $loja->id ? 'selected' : ''}}>{{$loja->nome}}</option>
                                                @empty
                                                <option value="">Nenhuma situação da conta encontrada</option>
                                                @endforelse
                                            </select>
                                            <div class="invalid-feedback">Example invalid select feedback</div>

                                        </div>
                                    </div>
                                </div>
                                <!-- <div class="row gx-3">
                                    <div class="col-md-11">
                                        <div class="mb-3">
                                            <select class="form-select" required="" aria-label="select example">
                                                <option value="">Selecciona a Loja</option>
                                                <option value="1">One</option>
                                                <option value="2">Two</option>
                                                <option value="3">Three</option>
                                            </select>
                                            <div class="invalid-feedback">Example invalid select feedback</div>

                                        </div>
                                    </div>
                                </div> -->
                                <div class="col-md-11">
                                    <div class="mb-3">
                                        <label class="form-label">Endereço</label>
                                        <input type="text" name="endereco" class="form-control" required placeholder="Nome do Funcionário" />
                                        <input type="hidden" name="password" class="form-control" value="123456789" />
                                    </div>
                                </div>
                                <div class="col-xl-11">
                                    <div class="card">
                                        <div class="card-body">
                                            <h5 class="card-title">Upload de Imagem</h5>
                                            <input type="file" id="input-file-now-custom-1" name="img" class="dropify" data-default-file="" />
                                        </div>
                                    </div>
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
        @endif

    </div>
    <!-- End Page-content -->


    @include('BackEnd.layout.footer')
</div>

@endsection