# backend_hackaton
1. Crie um ambiente virtual usando o [PDM](https://pdm.fming.dev/):

   ```
   pdm install
   ```

2. Intale o Redis:

   ```
   sudo apt install redis
   ```

3. Execute o servidor de desenvolvimento:

   ```
   pdm run dev
   ```


4. Certifique-se de que o websocket está rodando:

    ```
    redis-cli ping
    ```
    caso reotorne `PONG` tudo esta OK


5. Execute o websocket:

    ```
    cd src/
    pdm run daphne -p 8001 config.asgi:application
    ```