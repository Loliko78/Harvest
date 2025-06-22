@echo off
chcp 65001 >nul
echo.
echo ========================================
echo    🚀 HARVEST - Запуск приложения
echo ========================================
echo.
echo Выберите способ запуска:
echo.
echo 1. Локальный доступ (только на этом компьютере)
echo 2. Сетевой доступ (другие устройства в сети)
echo 3. Ngrok туннель (публичный доступ)
echo 4. Cloudflare туннель (публичный доступ)
echo 5. Localtunnel (публичный доступ, работает в России)
echo 6. Serveo (публичный доступ, без установки)
echo 7. Автоматический выбор (рекомендуется)
echo.
set /p choice="Введите номер (1-7): "

if "%choice%"=="1" (
    echo.
    echo 🚀 Запуск локального режима...
    python run_local.py
) else if "%choice%"=="2" (
    echo.
    echo 🚀 Запуск сетевого режима...
    python run_network.py
) else if "%choice%"=="3" (
    echo.
    echo 🚀 Запуск с Ngrok...
    python run_with_ngrok.py
) else if "%choice%"=="4" (
    echo.
    echo 🚀 Запуск с Cloudflare...
    python run_with_cloudflare.py
) else if "%choice%"=="5" (
    echo.
    echo 🚀 Запуск с Localtunnel...
    python run_with_localtunnel.py
) else if "%choice%"=="6" (
    echo.
    echo 🚀 Запуск с Serveo...
    python run_with_serveo.py
) else if "%choice%"=="7" (
    echo.
    echo 🚀 Автоматический выбор...
    python run_any.py
) else (
    echo.
    echo ❌ Неверный выбор. Запускаем автоматический режим...
    python run_any.py
)

pause 