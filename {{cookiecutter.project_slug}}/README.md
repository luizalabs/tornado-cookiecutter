{{ set sanitize_name=cookiecutter.project_name.lower()|replace(' ', '-')|replace('_', '-') }}

# {{cookiecutter.project_name}}
> {{cookiecutter.short_description}}

[![Build Status][travis-image]][travis-url]

{{cookiecutter.description}}

![](header.png)

## Instalação

OS X & Linux:

```sh
npm install my-crazy-module --save
```

## Exemplo de uso

Alguns exemplos motivamentes e úteis sobre como seu projeto pode ser utilizado. Adicionei blocos de códigos e, se necessário, screenshots.

## Configuração para Desenvolvimento

Crie e ative um ambiente virtual

```sh
mkvirtualenv {{sanitize_name}}
```

```sh
make install-dev
npm test
```

## Changelog

* 0.2.1
    * MUDANÇA: Atualização de docs (código do módulo permanece inalterado)
* 0.2.0
    * MUDANÇA: Remove `setDefaultXYZ()`
    * ADD: Adiciona `init()`
* 0.1.1
    * CONSERTADO: Crash quando chama `baz()` (Obrigado @NomeDoContribuidorGeneroso!)
* 0.1.0
    * O primeiro lançamento adequado
    * MUDANÇA: Renomeia `foo()` para `bar()`
* 0.0.1
    * Trabalho em andamento

## Meta

Seu Nome – [@SeuNome](https://twitter.com/...) – SeuEmail@exemplo.com

Distribuído sob a licença XYZ. Veja `LICENSE` para mais informações.

[https://github.com/yourname/github-link](https://github.com/othonalberto/)

[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/{{cookiecutter.travis_url}}
