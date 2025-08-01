package com.example.geminiretrofit

import retrofit2.http.Body
import retrofit2.http.POST

interface ApiService {
    @POST("/ask")
    suspend fun getApiResponse(
        @Body request: MyApiRequest // This sends a JSON body
    ): MyApiResponse
}
