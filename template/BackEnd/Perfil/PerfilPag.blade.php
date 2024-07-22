@extends('BackEnd.app')

@section('Conteudo')
<div class="main-content">

    <div class="page-content">
        <div class="container-fluid">
            <!-- start page title -->
            <div class="row">
                <div class="col-12">
                    <div class="page-title-box d-flex align-items-center justify-content-between">
                        <h4 class="mb-0 font-size-18">Perfil</h4>

                        <div class="page-title-right">
                            <ol class="breadcrumb m-0">
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Azul Claros</a></li>
                                <li class="breadcrumb-item"><a href="javascript: void(0);">Pages</a></li>
                                <li class="breadcrumb-item active">Perfil</li>
                            </ol>
                        </div>

                    </div>
                </div>
            </div>
            <!-- end page title -->
            @if (Auth()->user()->type==0)
            <div class="row">
                <div class="col-xl-3">
                    <div class="card profile">
                        <div class="card-body">
                            <div class="text-center">
                                <img src="assets/images/users/user-3.jpg" alt="" class="rounded-circle img-thumbnail avatar-xl">
                                <div class="online-circle">
                                    <i class="fa fa-circle text-success"></i>
                                </div>
                                <h4 class="mt-3">{{$UserData->username}}</h4>
                                @if ($UserData->type == 0)
                                <p class="text-muted font-size-13">Administrador</p>
                                @elseif($UserData->type == 1)
                                <p class="text-muted font-size-13">Funcionário</p>
                                @else
                                <p class="text-muted font-size-13">Cliente</p>
                                @endif
                                <ul class="list-unstyled list-inline mt-3 text-muted">
                                    <li class="list-inline-item font-size-13 me-3">
                                        <ul class="nav nav-tabs nav-tabs-custom" role="tablist">

                                            <li class="nav-item">
                                                <a class="btn btn-pink btn-round px-5" data-bs-toggle="tab" href="#settings" role="tab">Editar</a>
                                            </li>
                                        </ul>
                                    </li>

                                </ul>

                            </div>
                        </div>
                    </div>
                    <!-- end card -->

                    <!-- <div class="card">
                        <div class="card-body">
                            <h5>Personal Information</h5>
                            <h6>About :</h6>
                            <p class="card-title-desc">Hi I'm Mark Kearney,has
                                been the industry's standard dummy text ever since the 1500s,
                                when an unknown printer took a galley of type.
                            </p>
                            <hr>
                            <div class="button-list btn-social-icon">
                                <button type="button" class="btn btn-facebook rounded-circle">
                                    <i class="fab fa-facebook"></i>
                                </button>

                                <button type="button" class="btn btn-twitter rounded-circle ms-2">
                                    <i class="fab fa-twitter"></i>
                                </button>

                                <button type="button" class="btn btn-linkedin rounded-circle  ms-2">
                                    <i class="fab fa-linkedin"></i>
                                </button>

                                <button type="button" class="btn btn-dribbble rounded-circle  ms-2">
                                    <i class="fab fa-dribbble"></i>
                                </button>
                            </div>
                        </div>
                    </div> -->
                    <!-- end card -->



                </div>
                <!-- end col -->

                <div class="col-xl-9">

                    <div class="">
                        <div class="custom-tab tab-profile">

                            <!-- Nav tabs -->
                            <!-- <ul class="nav nav-tabs nav-tabs-custom" role="tablist">

                                <li class="nav-item">
                                    <a class="nav-link pb-3 pt-0" data-bs-toggle="tab" href="#settings" role="tab"><i class="fas fa-cog me-2"></i>Settings</a>
                                </li>
                            </ul> -->

                            <!-- Tab panes -->
                            <div class="tab-content pt-4">
                                <div class="tab-pane" id="settings" role="tabpanel">
                                    <div class="card">
                                        <div class="card-body">
                                            <div class="row">
                                                <div class="col-lg-12">
                                                    <div class="">
                                                        <form class="form-horizontal form-material mb-0" action="{{Route('Admin.Actualizar')}}" method="post" enctype="multipart/form-data">
                                                            @csrf
                                                            <input type="file" id="input-file-now-custom-1" class="dropify" data-default-file="{{url('assets/images/users/user-3.jpg')}}" />

                                                            <div class="mb-3">
                                                                <input type="text" placeholder="Nome de Utilizador" name="username" value="{{$UserData->username}}" class="form-control">
                                                            </div>

                                                            <div class="row">
                                                                <div class="col-md-4 mb-3">
                                                                    <input type="password" placeholder="Antiga Senha" name="oldpassword" class="form-control" id="example-email">
                                                                </div>
                                                                <div class="col-md-4 mb-3">
                                                                    <input type="password" placeholder="Nova Senha" name="newpassword" class="form-control">
                                                                </div>
                                                                <div class="col-md-4 mb-3">
                                                                    <input type="password" name="confirm_password" class="form-control" placeholder="Confirmar Senha">
                                                                </div>
                                                            </div>
                                                            <div class="row">
                                                                <div class="col-md-6 mb-3">
                                                                    <input type="email" placeholder="Email" name="email" class="form-control">
                                                                </div>
                                                                <!-- <div class="col-md-6 mb-3">
                                                                    <select class="form-control">
                                                                        <option>London</option>
                                                                        <option>India</option>
                                                                        <option>Usa</option>
                                                                        <option>Canada</option>
                                                                        <option>Thailand</option>
                                                                    </select>
                                                                </div> -->
                                                            </div>
                                                            <div class="mb-3">
                                                                <textarea rows="5" placeholder="Message" class="form-control"></textarea>
                                                                <button class="btn btn-primary btn-sm text-light px-4 mt-3 float-end mb-0">Editar
                                                                    Perfil</button>
                                                            </div>
                                                        </form>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            @elseif(Auth()->user()->type==1) <!-- FUNCIONARIO -->
            <div class="row">
                <div class="col-xl-3">
                    <div class="card profile">
                        <div class="card-body">
                            <div class="text-center">
                                @foreach ($FuncDatas as $FuncData)

                                <img src="{{ (!empty($FuncData->img)) ? url($FuncData->img) : '' }}" alt="" class="rounded-circle img-thumbnail avatar-xl">
                                @endforeach
                                <div class="online-circle">
                                    <i class="fa fa-circle text-success"></i>
                                </div>
                                <h4 class="mt-3">{{$UserData->username}}</h4>
                                @if ($UserData->type == 0)
                                <p class="text-muted font-size-13">Administrador</p>
                                @elseif($UserData->type == 1)
                                <p class="text-muted font-size-13">Funcionário</p>
                                @else
                                <p class="text-muted font-size-13">Cliente</p>
                                @endif
                                <ul class="list-unstyled list-inline mt-3 text-muted">
                                    <li class="list-inline-item font-size-13 me-3">
                                        <ul class="nav nav-tabs nav-tabs-custom" role="tablist">

                                            <li class="nav-item">
                                                <a class="btn btn-pink btn-round px-5" data-bs-toggle="tab" href="#settings" role="tab">Editar</a>
                                            </li>
                                        </ul>
                                    </li>

                                </ul>

                            </div>
                        </div>
                    </div>
                    <!-- end card -->
                </div>
                <!-- end col -->

                <div class="col-xl-9">

                    <div class="">
                        <div class="custom-tab tab-profile">

                            <!-- Nav tabs -->
                            <!-- <ul class="nav nav-tabs nav-tabs-custom" role="tablist">

                                <li class="nav-item">
                                    <a class="nav-link pb-3 pt-0" data-bs-toggle="tab" href="#settings" role="tab"><i class="fas fa-cog me-2"></i>Settings</a>
                                </li>
                            </ul> -->

                            <!-- Tab panes -->
                            <div class="tab-content pt-4">
                                <div class="tab-pane" id="settings" role="tabpanel">
                                    <div class="card">
                                        <div class="card-body">
                                            <div class="row">
                                                <div class="col-lg-12">
                                                    <div class="">
                                                        @foreach ($FuncDatas as $FuncData)
                                                        <form class="form-horizontal form-material mb-0" action="{{Route('Func.Actualizar')}}" method="post" enctype="multipart/form-data">
                                                            @csrf
                                                            <input type="file" id="input-file-now-custom-1" name="img" class="dropify" data-default-file="{{ (!empty($FuncData->img)) ? url($FuncData->img) : '' }}" />

                                                            <div class="mb-3">
                                                                <input type="text" placeholder="Nome de Utilizador" name="username" value="{{$FuncData->username}}" class="form-control">
                                                            </div>
                                                            <div class="mb-3">
                                                                <input type="text" placeholder="Nome Completo" name="nome" value="{{$FuncData->nome}}" class="form-control">
                                                            </div>

                                                            <div class="row">
                                                                <div class="col-md-4 mb-3">
                                                                    <input type="password" placeholder="Antiga Senha" name="oldpassword" class="form-control" id="example-email">
                                                                </div>
                                                                <div class="col-md-4 mb-3">
                                                                    <input type="password" placeholder="Nova Senha" name="newpassword" class="form-control">
                                                                </div>
                                                                <div class="col-md-4 mb-3">
                                                                    <input type="password" name="confirm_password" class="form-control" placeholder="Confirmar Senha">
                                                                </div>
                                                            </div>
                                                            <div class="row">
                                                                <div class="col-md-4 mb-3">
                                                                    <input type="text" placeholder="Número de Tel" value="{{ $FuncData->numero}}" name="numero" class="form-control" id="example-email">
                                                                </div>
                                                                <div class="col-md-4 mb-3">
                                                                    <input type="text" placeholder="Endereço" value="{{ $FuncData->endereco}}" name="endereco" class="form-control">
                                                                </div>
                                                                <div class="col-md-4 mb-3">
                                                                    <input class="form-control" type="date" value="{{$FuncData->dataNasc}}" name="dataNasc" value="Ano-Mes-Dia" id="example-date-input">

                                                                </div>
                                                            </div>
                                                            <div class="row">
                                                                <div class="col-md-6 mb-3">
                                                                    <input type="email" placeholder="Email" name="email" class="form-control">
                                                                </div>
                                                                <div class="col-md-6 mb-3">
                                                                    <select class="form-control" name='genero'>
                                                                        <option {{ $FuncData->genero=='F' ? 'selected' : ''}}>F</option>
                                                                        <option {{ $FuncData->genero=='M' ? 'selected' : ''}}>M</option>
                                                                    </select>
                                                                </div>
                                                            </div>
                                                            <div class="mb-3">
                                                                <button class="btn btn-primary btn-sm text-light px-4 mt-3 float-end mb-0">Editar
                                                                    Perfil</button>
                                                            </div>
                                                        </form>
                                                        @endforeach
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            @else <!-- CLIENTE -->
            <div class="row">
                <div class="col-xl-3">
                    <div class="card profile">
                        <div class="card-body">
                            <div class="text-center">
                                <img src="assets/images/users/user-3.jpg" alt="" class="rounded-circle img-thumbnail avatar-xl">
                                <div class="online-circle">
                                    <i class="fa fa-circle text-success"></i>
                                </div>
                                <h4 class="mt-3">{{$UserData->username}}</h4>
                                @if ($UserData->type == 0)
                                <p class="text-muted font-size-13">Administrador</p>
                                @elseif($UserData->type == 1)
                                <p class="text-muted font-size-13">Funcionário</p>
                                @else
                                <p class="text-muted font-size-13">Cliente</p>
                                @endif
                                <ul class="list-unstyled list-inline mt-3 text-muted">
                                    <li class="list-inline-item font-size-13 me-3">
                                        <ul class="nav nav-tabs nav-tabs-custom" role="tablist">

                                            <li class="nav-item">
                                                <a class="btn btn-pink btn-round px-5" data-bs-toggle="tab" href="#settings" role="tab">Editar</a>
                                            </li>
                                        </ul>
                                    </li>

                                </ul>

                            </div>
                        </div>
                    </div>
                    <!-- end card -->

                    <!-- <div class="card">
                        <div class="card-body">
                            <h5>Personal Information</h5>
                            <h6>About :</h6>
                            <p class="card-title-desc">Hi I'm Mark Kearney,has
                                been the industry's standard dummy text ever since the 1500s,
                                when an unknown printer took a galley of type.
                            </p>
                            <hr>
                            <div class="button-list btn-social-icon">
                                <button type="button" class="btn btn-facebook rounded-circle">
                                    <i class="fab fa-facebook"></i>
                                </button>

                                <button type="button" class="btn btn-twitter rounded-circle ms-2">
                                    <i class="fab fa-twitter"></i>
                                </button>

                                <button type="button" class="btn btn-linkedin rounded-circle  ms-2">
                                    <i class="fab fa-linkedin"></i>
                                </button>

                                <button type="button" class="btn btn-dribbble rounded-circle  ms-2">
                                    <i class="fab fa-dribbble"></i>
                                </button>
                            </div>
                        </div>
                    </div> -->
                    <!-- end card -->



                </div>
                <!-- end col -->

                <div class="col-xl-9">

                    <div class="">
                        <div class="custom-tab tab-profile">

                            <!-- Nav tabs -->
                            <!-- <ul class="nav nav-tabs nav-tabs-custom" role="tablist">

                                <li class="nav-item">
                                    <a class="nav-link pb-3 pt-0" data-bs-toggle="tab" href="#settings" role="tab"><i class="fas fa-cog me-2"></i>Settings</a>
                                </li>
                            </ul> -->

                            <!-- Tab panes -->
                            <div class="tab-content pt-4">
                                <div class="tab-pane" id="settings" role="tabpanel">
                                    <div class="card">
                                        <div class="card-body">
                                            <div class="row">
                                                <div class="col-lg-12">
                                                    <div class="">
                                                        <form class="form-horizontal form-material mb-0" action="{{Route('Admin.Actualizar')}}" method="post" enctype="multipart/form-data">
                                                            @csrf
                                                            <input type="file" id="input-file-now-custom-1" class="dropify" data-default-file="{{url('assets/images/users/user-3.jpg')}}" />

                                                            <div class="mb-3">
                                                                <input type="text" placeholder="Nome de Utilizador" name="username" value="{{$UserData->username}}" class="form-control">
                                                            </div>

                                                            <div class="row">
                                                                <div class="col-md-4 mb-3">
                                                                    <input type="password" placeholder="Antiga Senha" name="oldpassword" class="form-control" id="example-email">
                                                                </div>
                                                                <div class="col-md-4 mb-3">
                                                                    <input type="password" placeholder="Nova Senha" name="newpassword" class="form-control">
                                                                </div>
                                                                <div class="col-md-4 mb-3">
                                                                    <input type="password" name="confirm_password" class="form-control" placeholder="Confirmar Senha">
                                                                </div>
                                                            </div>
                                                            <div class="row">
                                                                <div class="col-md-6 mb-3">
                                                                    <input type="email" placeholder="Email" name="email" class="form-control">
                                                                </div>
                                                                <!-- <div class="col-md-6 mb-3">
                                                                    <select class="form-control">
                                                                        <option>London</option>
                                                                        <option>India</option>
                                                                        <option>Usa</option>
                                                                        <option>Canada</option>
                                                                        <option>Thailand</option>
                                                                    </select>
                                                                </div> -->
                                                            </div>
                                                            <div class="mb-3">
                                                                <textarea rows="5" placeholder="Message" class="form-control"></textarea>
                                                                <button class="btn btn-primary btn-sm text-light px-4 mt-3 float-end mb-0">Editar
                                                                    Perfil</button>
                                                            </div>
                                                        </form>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            @endif


        </div>
        <!-- container-fluid -->
    </div>
    <!-- End Page-content -->


    @include('BackEnd.layout.footer')
</div>
@endsection