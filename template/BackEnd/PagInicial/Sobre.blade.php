@extends('BackEnd.app')

@section('Conteudo')

<div class="main-content">

    <div class="page-content">
        <div class="container-fluid">

            <!-- start page title -->
            <div class="row">
                <div class="col-12">
                    <div class="page-title-box d-flex align-items-center justify-content-between">
                        <h4 class="mb-0 font-size-18">Sobre Nós</h4>

                        <div class="page-title-right">
                            <ol class="breadcrumb m-0">
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Azul Claros</a></li>
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Forms</a></li>
                                <li class="breadcrumb-item active">Sobre Nós</li>
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

                            <form class="custom-validation" action="{{route('Sobre.Actualizar')}}" method="POST" enctype="multipart/form-data">
                                @csrf
                                <div class="col-md-6">
                                    <div class="mb-3">
                                        <label class="form-label">Titulo</label>
                                        <input type="text" class="form-control" name="titulo" value="{{$Sobre->titulo}}" />
                                        <input type="hidden" class="form-control" name="id" value="{{$Sobre->id}}" />
                                    </div>
                                </div>
                                <div class="mb-3">
                                    <label class="form-label">Descrição</label>
                                    <div>
                                        <textarea required name="descricao" class="form-control" rows="5" data-parsley-id="21" aria-describedby="parsley-id-21">{{$Sobre->descricao}}</textarea>
                                        <ul class="parsley-errors-list" id="parsley-id-21" aria-hidden="false">
                                            <li class="parsley-required">This value is required.</li>
                                        </ul>
                                    </div>
                                </div>

                                <div class="col-xl-12">
                                    <div class="card">
                                        <div class="card-body">
                                            <h5 class="card-title">Upload de Imagem</h5>
                                            <input type="file" id="input-file-now-custom-1" name="img" class="dropify" data-default-file="{{url($Sobre->img)}}" />
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
        </div>
        <!-- container-fluid -->
    </div>
    <!-- End Page-content -->


    @include('BackEnd.layout.footer')
</div>

@endsection