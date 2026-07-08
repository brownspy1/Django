/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",// searce in all temlats foldar
    "./**/templates/**/*.html" // templat insaid app
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

