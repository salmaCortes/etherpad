const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/etherpad',
    createProxyMiddleware({
      target: 'http://localhost:9001/api/1',  // URL de tu servidor Etherpad
      changeOrigin: true,
      pathRewrite: {
        '^/etherpad': '',  // Puedes ajustar la ruta según sea necesario
      },
      secure: false,  // Si no estás usando HTTPS
    })
  );
};
