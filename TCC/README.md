
# TCC — Aplicativo de Monitoramento de Áreas de Risco de Dengue

**Curso:** Bacharelado em Engenharia da Computação — UNIVESP

## 🎯 Objetivo do Projeto

Desenvolver um aplicativo multiplataforma, utilizando Flutter, que disponibiliza um mapa interativo da cidade de São Paulo com a localização dos casos de dengue. O principal propósito é alertar o usuário, em tempo real, ao adentrar regiões classificadas como áreas de risco elevado para o contágio da doença.

## 🗺️ Funcionalidades Principais

- Visualização de mapa da cidade de São Paulo com pontos de incidência de casos de dengue.
- Alerta automático ao usuário ao entrar em zonas de risco elevado, com base em sua localização.
- Interface intuitiva e responsiva, adequada para dispositivos móveis.
- Atualização dinâmica dos dados de contágio.

## 🔗 Integração com Dados em Tempo Real

O aplicativo integra-se a um sistema de coleta automática de dados, desenvolvido em Python, responsável por realizar web scraping em fontes oficiais e confiáveis. Esse scraper coleta e atualiza periodicamente as informações sobre casos de dengue, garantindo que o usuário tenha acesso a dados recentes e relevantes para sua segurança.

## 📦 Estrutura do Projeto

- **api_namira.py / extrator.py:** Scripts Python para extração e atualização dos dados de contágio.
- **Dados/**: Armazenamento dos dados coletados (JSON, PDF, etc.).
- **NaMira/**: Código-fonte do aplicativo Flutter.

## 🏆 Relevância

Este projeto visa contribuir para a saúde pública, promovendo a conscientização e prevenção do contágio por dengue, utilizando tecnologia de geolocalização e integração de dados em tempo real.

---

**Desenvolvido por [Seu Nome] — UNIVESP**
