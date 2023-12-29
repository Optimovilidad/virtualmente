const ping = require('ping');
const { exec } = require('child_process');

const checkInternetConnection = () => {
    return new Promise((resolve) => {
        ping.sys.probe('www.google.com', (isAlive) => {
            resolve(isAlive);
        });
    });
};

const playMusicInVLC = () => {
    const vlcCommand = 'vlc http://186.4.224.169:8080/livestream/stream.m3u8';
    exec(vlcCommand, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error al reproducir música en VLC: ${error.message}`);
        } else {
            console.log(`Reproduciendo música en VLC:\n${stdout}`);
        }
    });
};

const stopMusicInVLC = () => {
    // Enviar señal de interrupción (CTRL+C) para detener VLC
    //para cerrar en linux
    //exec('pkill -2 vlc', (error, stdout, stderr) => {
    exec('taskkill /IM vlc.exe', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error al detener VLC: ${error.message}`);
        } else {
            console.log('VLC detenido.');
        }
    });
};

const main = async () => {
    let musicPlaying = false;

    while (true) {
        const isConnected = await checkInternetConnection();

        if (isConnected) {
            if (!musicPlaying) {
                // Hay conexión a Internet y la música no está reproduciéndose, reproducir música en VLC
                console.log('Conexión a Internet establecida. Reproduciendo música en VLC...');
                playMusicInVLC();
                musicPlaying = true;
            }
        } else {
            if (musicPlaying) {
                // Se perdió la conexión y la música está reproduciéndose, detener VLC
                console.log('Se perdió la conexión a Internet. Deteniendo VLC...');
                await new Promise((resolve) => setTimeout(resolve, 10000));
                stopMusicInVLC();
                musicPlaying = false;
            }

            // No hay conexión a Internet, esperar 10 segundos
            console.log('No hay conexión a Internet. Intentando de nuevo en 10 segundos...');
            await new Promise((resolve) => setTimeout(resolve, 10000));
        }
    }
};

main();
