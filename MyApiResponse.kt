package com.example.geminiretrofit

import com.google.gson.annotations.SerializedName

// CHANGE THIS ENTIRE CLASS: It needs to match the server's JSON response
data class MyApiResponse(
    @SerializedName("status")
    val status: String,

    @SerializedName("response_text")
    val responseText: String
)