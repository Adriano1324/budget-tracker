import { type TypedDocumentString } from "@/graphql/generated/graphql";

export const executeGraphql = async <TResult, TVariables>(
    query: TypedDocumentString<TResult, TVariables>,
    options?: {
        variables?: TVariables;
        headers?: HeadersInit;
        next?: NextFetchRequestConfig;
        cache?: RequestCache;
    },
): Promise<TResult> => {
    const url = process.env.GRAPHQL_URL;

    if (!url) {
        throw TypeError("GRAPHQL_URL is not defined");
    }

    const res = await fetch(url, {
        method: "POST",
        body: JSON.stringify({
            query,
            variables: options?.variables,
        }),
        headers: {
            "Content-Type": "application/json",
            ...options?.headers,
        },
        next: options?.next,
        cache: options?.cache,
    });

    type GraphQLResponse<T> = { data?: undefined; errors: { message: string }[] } | { data: T; errors?: undefined };

    const graphqlResponse = (await res.json()) as GraphQLResponse<TResult>;

    if (graphqlResponse.errors) {
        throw TypeError(`GraphQL Error`, { cause: JSON.stringify(graphqlResponse.errors, null, 2) });
    }

    return graphqlResponse.data;
};
