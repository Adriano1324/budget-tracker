import { loadEnvConfig } from "@next/env";
import type { CodegenConfig } from "@graphql-codegen/cli";

loadEnvConfig(process.cwd());

const config: CodegenConfig = {
    schema: process.env.GRAPHQL_URL,
    overwrite: true,
    // ignoreNoDocuments: true,
    documents: ["./graphql/**/*.gql"],
    generates: {
        "./graphql/generated/": {
            preset: "client",
            presetConfig: {
                // fragmentMasking: { unmaskFunctionName: "getFragmentData" },
                fragmentMasking: false,
            },
            config: {
                useTypeImports: true,
                enumsAsTypes: true,
                defaultScalarType: "unknown",
                skipTypename: true,
                documentMode: "string",
            },
        },
    },
};

// eslint-disable-next-line import/no-default-export
export default config;