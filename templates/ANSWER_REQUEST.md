# Answer Request

Request_ID: ANS-###
User_question:
Intent: RECALL_RESULT | EXPLAIN_SIMPLE | EXPLAIN_TECHNICAL | EXPLAIN_RIGOROUS | EXPLAIN_PAPER | SUMMARIZE | COMPARE | LIST_ASSUMPTIONS | LIST_LIMITATIONS | SHOW_PROOF | SHOW_DEPENDENCIES | WHY_TRUE | WHY_FALSE | WHAT_REMAINS_OPEN | NEXT_STEP | TEACH | REFRESH_EVIDENCE | RESEARCH_NEW
Depth: simple | technical | rigorous | paper
Question_scope:
Memory_tags:
Certificates_to_load:
Graph_nodes_to_load:
Needs_internal_source: yes | no
Needs_external_refresh: yes | no
Needs_research_loop: yes | no
Requested_output_format:
Sufficiency_status: sufficient | expand_graph | open_source | refresh_external | new_research

Regla: elegir siempre la opción de menor costo de contexto que permita responder fielmente. No activar new_research si la respuesta ya está contenida en un resultado certificado vigente.