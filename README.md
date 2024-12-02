# backend_hackaton
1. Crie um ambiente virtual usando o [PDM](https://pdm.fming.dev/):

   ```
   pdm install
   ```

2. Execute o servidor de desenvolvimento:

   ```
   pdm run dev
   ```

3. Execute o websocket:

    ```
    cd src/
    pdm run daphne -p 8001 config.asgi:application
    ```