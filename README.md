# mformatting-posts

Artes e legendas dos posts do Instagram @mformatting (Rolândia/PR), publicados via Metricool.

- `posts/` — imagens publicadas (1080x1350). O Metricool busca daqui pelo link raw.
- `gerador/render.py` — gera as artes: `python3 gerador/render.py lote.json posts`
- `gerador/historico.json` — todos os posts já feitos (tema, título, itens, legenda, data). Não repetir temas.

Formato de cada post: `slug`, `tag` (ex. "// MANUTENÇÃO"), `title`, `items` (4–5 itens curtos), `caption`.
Temas: manutenção de PC, sites, aparecer no Google, IA como ajuda no trabalho (nunca como "criação de site"), linguagens de programação, segurança/backup, tecnologia em geral.
