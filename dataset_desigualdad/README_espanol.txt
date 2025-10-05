Título: Index of Urban Inequality - Mexico
Descripción: Geospatial layer of access to urban infrastructure and equipment in cities of Mexico
Versión: 1
Fecha de Lanzamiento: 2021-02-25
URI: https://datasets.wri.org/dataset/index-urban-inequality-mexico
Derechos de Autor: World Resources Institute México 2021
Licencia: Creative Commons Attribution 4.0 International (CC-BY-4)
Contacto: Mauricio Brito (mauricio.brito@wri.org)
Citación: Brito, M., Macias, J., Ramírez Reyes, L., Jacquin C., y Zubicaray, G. 2021. “Índice de Desigualdad Urbana.” Documento de Trabajo. Ciudad de México: World Resources Institute México. Disponible en https://wrimexico.org/publication/indice-de-desigualdad-urbana


Extracto:

El objetivo fundamental de la metodología del IDU consiste en estimar el nivel de proximidad a satisfactores urbanos con el que cuentan los diferentes estratos socioeconómicos en las ciudades. Permite comparar e identificar la desigualdad en la distribución territorial de las oportunidades de desarrollo como el empleo formal, educación y salud públicas entre otras. Este dataset incluye los resultados del análisis propuesto en el Documento de Trabajo “Índice de Desigualdad Urbana” realizados a nivel manzana urbana para las 74 zonas metropolitanas en México, esto con base en el Marco Geoestadístico 2010 versión 4.3 (Censo de Población y Vivienda 2010), y su accesibilidad geográfica a oportunidades de desarrollo en la ciudad; empleo formal (Censos Económicos 2014 INEGI), educación pública de nivel básico, medio y superior (DENUE 2019 INEGI), salud pública (Secretaría de Salud 2019), abasto (DENUE 2019 INEGI), espacio abierto (Marco Geoestadístico 2018 INEGI), instalaciones culturales públicas (DENUE 2019 INEGI), estaciones de transporte público masivo (WRI México 2020), e incluyendo el IISU (WRI 2021), disponible en https://wrimexico.org/publication/indice-de-desigualdad-urbana.


Indicadores:

- cve_ent    : [string] Clave Geoestadística Entidad Federativa
- cve_mun    : [string] Clave Geoestadística Municipal
- cve_sun    : [string] Clave Ciudad Sistema Urbano Nacional (SUN)
- cvegeo     : [string] Clave Geoestadística Manzana Urbana
- sun        : [string] Nombre de la Ciudad Sistema Urbano Nacional (SUN)
- gmu        : [string] Grado de Marginación Urbana (CONAPO)
- iisu_sun   : [string] índice de Inclusión Social Urbana (Nivel Nacional)
- iisu_cd    : [string] índice de Inclusión Social Urbana (Nivel Ciudad)
- Pob_2010   : [integer] Población 2010
- Empleo     : [real] Empleos formales accesibles en 30 minutos (Peatonal y/o Transporte Público Masivo)
- E_basica   : [real] Escuelas públicas de educación básica accesibles en 15 minutos (Peatonal y/o Transporte Público Masivo)
- E_media    : [real] Escuelas públicas de educación media superior accesibles en 30 minutos (Peatonal y/o Transporte Público Masivo)
- E_superior : [real] Escuelas públicas de educación superior accesibles en 30 minutos (Peatonal y/o Transporte Público Masivo)
- Salud_cama : [real] Escuelas públicas de educación superior accesibles en 30 minutos (Peatonal y/o Transporte Público Masivo)
- Salud_cons : [real] Consultorios médicos públicos accesibles en 30 minutos (Peatonal y/o Transporte Público Masivo)
- Abasto     : [real] Unidades económicas de abasto accesibles en 20 minutos (Peatonal y/o Transporte Público Masivo)
- Espacio_ab : [real] m2 de espacio abierto accesibles en 20 minutos (Peatonal y/o Transporte Público Masivo)
- Cultura    : [real] Instalaciones culturales públicas accesibles en 20 minutos (Peatonal y/o Transporte Público Masivo)
- Est_Tpte   : [real] Estaciones del sistema de transporte público masivo accesibles en 15 minutos (Peatonal y/o Transporte Público Masivo)


Consideración:

El indicador `Est_Tpte` solo se calcula para las siguientes ciudades:

M02.03 - Tijuana
M08.01 - Chihuahua
M08.04 - Juárez
M09.01 - Valle de México
M11.03 - León
M12.01 - Acapulco
M13.01 - Pachuca
M14.01 - Guadalajara
M19.01 - Monterrey
M21.01 - Puebla-Tlaxcala
M22.01 - Querétaro

Otras ciudades tienen valor de 0 para el indicador `Est_Tpte`. Ya que no cuentan con un sistema de transporte público masivo (metro, BRT, tren ligero y tren suburbano).

