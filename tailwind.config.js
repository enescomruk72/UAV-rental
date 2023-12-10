/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './templates/**/*.{html,js}',
      './apps/**/*.{py,}',
      './static/**/*.{js,}\''
  ],
  theme: {
      fontFamily: {
          'default': ['Montserrat'],
      },
      fontWeight: {
          light: '300',
          regular: '400',
          medium: '500',
          semibold: '600',
          bold: '700',
      },
      extend: {
          colors: {
              'primary': '#111C4E',
              'dark': '#333333',
              'white': '#ffffff',
              'gray': '#333333',
              'lightgray': '#F8F8F8',
              'lightgrayd': '#F1F1F1',
              'lightgraye': '#C9C9C9',
              'lightgrayf': '#ECECEC',
              'lightgrayg': '#8E8E8E',
              'lightgrayh': '#DFDFDF',
              'lightgrayi': '#7E7E7E',
              'lightgrayj': '#DAE0EB',
              'hoverblue': '#2266BB',
              'darkred': '#FF0000',
              'success': '#22A900',
              'lightblue': '#E9F0F8',
              'orange': '#F88300',
              'star': '#FFB057',
              'nav-black': '#000'
          },
          padding: {
              '1.5': '6px',
              '2.5': '10px'
          },
          borderRadius: {
              '5px': '5px'
          },
          gap: {
              '5px': '5px'
          },
          fontSize: {
              '15': '15px'
          },
      },
      screens: {
          'xs': '500px',

          'sm': '640px',
          // => @media (min-width: 640px) { ... }

          'md': '768px',
          // => @media (min-width: 768px) { ... }

          'lg': '1280px',
          // => @media (min-width: 1024px) { ... }

          'xl': '1300px',
          // => @media (min-width: 1280px) { ... }

          '2xl': '1536px',
          // => @media (min-width: 1536px) { ... }

      },
  },
  plugins: [],
}