@echo off
chcp 65001 > nul

color 1
echo ░██████╗███████╗████████╗██╗░░░██╗██████╗░
color 2
echo ██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗
color 3
echo ╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝
color 4
echo ░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░
color 1
echo ██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░
color 2
echo ╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░

echo Deseja instalar as dependências [S/N]?

set /p op=_

if /i "%op%"=="S" (
    pip install -q -U flask
    pip install -q -U colorama
    pip install -q -U pandas
    pip install -q -U numpy
    pip install -q -U requests
    pip install -q -U hashlib
    echo Pacotes instalados com sucesso!
) else (
    color 4
    echo Não foi instalado nenhum pacote.
    pause
)

echo Deseja instalar as variáveis de ambiente [S/N]?

set /p op2=_

if /i "%op2%"=="S" (
    :: Define o caminho absoluto para o diretório OpenSSL
    set "OPENSSL_DIR=%~dp0sources\OpenSSL-Win64\bin"
    
    :: Define o caminho absoluto para o diretório Hydra
    set "HYDRA_DIR=%~dp0sources\thc-hydra-windows-v9.1"

    :: Adiciona os diretórios ao PATH
    setx PATH "%PATH%;%OPENSSL_DIR%;%HYDRA_DIR%"

    :: Mensagem de sucesso
    echo Variáveis de ambiente configuradas com sucesso!
) else (
    color 4
    echo Não foram configuradas variáveis de ambiente.
)

pause
