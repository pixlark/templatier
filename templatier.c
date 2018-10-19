#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "stretchy_buffer.h"

char * load_string_from_file(char * path)
{
	FILE * file = fopen(path, "r");
	if (file == NULL) return NULL;
	int file_len = 0;
	while (fgetc(file) != EOF) file_len++;
	char * str = (char*) malloc(file_len + 1);
	str[file_len] = '\0';
	fseek(file, 0, SEEK_SET);
	for (int i = 0; i < file_len; i++) str[i] = fgetc(file);
	fclose(file);
	return str;
}

typedef struct {
	char * start;
	char * end;
} Segment;

void template(char * text, size_t text_len)
{
	// 1. Find all @type directives and make table of types
	// 2. Segment text by @file directives
	Segment * directives = NULL;
	for (int i = 0; i < text_len - 1; i++) {
		if ((i == 0 && text[i] == '@') ||
			(text[i] == '\n' && text[i+1] == '@')) {
			printf("...%s...", text + i + 1);
			char * start = text + i + 1;
			char * end = NULL;
			for (int j = i + 1; j < text_len - 1; j++) {
				if (text[j] == '\n' || text[j] == EOF) {
					end = text + j;
					break;
				}
			}
			assert(end);
			sb_push(directives, ((Segment) { start, end }));
		}
	}
	for (int i = 0; i < sb_count(directives); i++) {
		printf("directive: '%.*s'\n", directives[i].end - directives[i].start, directives[i].start);
	}
}

int main(int argc, char ** argv)
{
	if (argc < 2) {
		printf("Provide at least one template file\n");
		return 1;
	}
	for (int i = 1; i < argc; i++) {
		char * text = load_string_from_file(argv[i]);
		template(text, strlen(text));
	}
	return 0;
}

