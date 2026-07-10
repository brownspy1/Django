/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",      // search in all templates folder
    "./**/templates/**/*.html",   // template inside app
    "./**/*.py",                  // Python files (forms.py, views.py etc.)
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

