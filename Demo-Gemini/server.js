// server.js
import 'dotenv/config';
import express from 'express';
import cors from 'cors';
import path from 'path';
import { fileURLToPath } from 'url';
import { GoogleGenerativeAI } from '@google/generative-ai';

// ───────────────────────────────────────────────────────────────
// Rutas y utilidades de Node (ESM)
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// ───────────────────────────────────────────────────────────────
// Validación de variables de entorno
const API_KEY = process.env.GOOGLE_AI_API_KEY || process.env.GEMINI_API_KEY; // acepta cualquiera
if (!API_KEY) {
  console.error('❌ Falta la variable de entorno GOOGLE_AI_API_KEY o GEMINI_API_KEY');
  process.exit(1);
}

const MODEL = process.env.GEMINI_MODEL || 'gemini-1.5-flash';

// ───────────────────────────────────────────────────────────────
// Inicialización de Express
const app = express();
app.use(cors());
app.use(express.json({ limit: '1mb' }));

// ───────────────────────────────────────────────────────────────
// Inicializa el cliente oficial de Gemini (@google/generative-ai)
const genAI = new GoogleGenerativeAI(API_KEY);
const model = genAI.getGenerativeModel({
  model: MODEL,
  // Si tu versión del SDK lo permite, puedes descomentar para usar instrucción de sistema:
  // systemInstruction: "Eres un asistente útil, conciso y en español. Si te piden código, respóndelo formateado."
});

// ───────────────────────────────────────────────────────────────
// Definir la ruta POST *antes* de los estáticos (evita 405)
app.post('/api/chat', async (req, res) => {
  try {
    const { message, history = [] } = req.body || {};
    if (typeof message !== 'string' || !message.trim()) {
      return res.status(400).json({ error: 'Mensaje inválido' });
    }

    const systemPreamble = 'Eres un asistente útil, conciso y en español. Si te piden código, respóndelo formateado.';

    // Convertimos el historial al formato de "contents"
    const contents = [
      // Si no usas systemInstruction, mete el preámbulo como primer turno:
      { role: 'user', parts: [{ text: systemPreamble }] },

      ...history.map((m) => ({
        role: m.role === 'assistant' ? 'model' : 'user',
        parts: [{ text: String(m.content || '') }],
      })),}

      { role: 'user', parts: [{ text: message }] },
    ];

    // Llamada no-streaming
    const result = await model.generateContent({ contents });

    // OJO: hay que obtener la Response y luego text()
    const response = await result.response;
    const text = response.text();

    return res.json({ text });
  } catch (err) {
    console.error('Error al consultar Gemini:', err);
    return res.status(500).json({ error: 'Fallo al consultar Gemini' });
  }
});

// ───────────────────────────────────────────────────────────────
// Estáticos DESPUÉS del endpoint
app.use(express.static(path.join(__dirname, 'public')));

// ───────────────────────────────────────────────────────────────
// Arranque del servidor
const port = process.env.PORT || 5500;
app.listen(port, () => {
  console.log(`Servidor listo en http://localhost:${port}`);
});
