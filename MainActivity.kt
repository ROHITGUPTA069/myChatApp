package com.example.geminiretrofit

import android.annotation.SuppressLint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.lifecycle.lifecycleScope
import com.example.geminiretrofit.R // Ensure this import is here
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {

    // Declare views as properties of the class
    private lateinit var promptEditText: EditText
    private lateinit var submitButton: Button
    private lateinit var outputTextView: TextView // Renamed for clarity

    @SuppressLint("SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Initialize views once when the activity is created
        promptEditText = findViewById(R.id.promptEditText)
        submitButton = findViewById(R.id.submitButton)
        outputTextView = findViewById(R.id.outputText) // <-- CORRECT ID HERE

        submitButton.setOnClickListener {
            val promptText = promptEditText.text.toString()
            if (promptText.isNotEmpty()) {
                // Inside the submitButton.setOnClickListener in MainActivity.kt

                lifecycleScope.launch {
                    try {
                        outputTextView.text = "Loading..."

                        // Use the corrected request class with the "prompt" parameter
                        val requestObject = MyApiRequest(prompt = promptText)

                        val response = RetrofitClient.apiService.getApiResponse(requestObject)

                        // Use the corrected response property: "responseText"
                        outputTextView.text = response.responseText

                    } catch (e: Exception) {
                        outputTextView.text = "Error: ${e.message}"
                    }
                }
            } else {
                promptEditText.error = "Please enter a prompt"
            }
        }
    }
}

