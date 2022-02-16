python3 tools/preprocess_data.py \
            --input /lambda_stor/data/pro/docs_per_line/all_shards.jsonl.zst \
            --output-prefix ./data/pro \
            --vocab-file ./data/20B_tokenizer.json \
            --dataset-impl mmap \
            --tokenizer-type HFTokenizer \
            --workers 80 \
	    --append-eod \
	    --num-docs 67466547
