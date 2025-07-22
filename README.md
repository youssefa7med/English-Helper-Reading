# English Reading Evaluation System 📚

![English Reading](https://www.longwood.edu/media/top-tier/news/2014/buzz/realinquirycat.gif)

An intelligent English reading comprehension and pronunciation evaluation system powered by AI that generates personalized reading passages with graduated difficulty levels and provides detailed performance assessments based on CEFR standards.

## 🚀 Live Demo

**Try it now:** [English Helper Reading - Live Demo](https://huggingface.co/spaces/YoussefA7med/English_Helper_Reading)

Experience the full functionality of the English Reading Evaluation System directly in your browser! No installation required.

## 🌟 Features

### 🎯 **Personalized Content Generation**
- Generate reading passages on any topic of interest
- AI-powered content creation using DeepSeek Chat API
- Engaging and educational content tailored for language learners

### 📊 **Graduated Difficulty Levels**
- **A1-A2 (Beginner)**: Simple sentences, basic vocabulary, present tense
- **B1 (Intermediate)**: Complex sentences, varied vocabulary, past/future tenses
- **B2 (Upper-Intermediate)**: Advanced grammar, academic vocabulary, conditional forms
- **C1-C2 (Advanced)**: Sophisticated language, complex ideas, advanced structures

### 🎙️ **Advanced Speech Recognition**
- Real-time audio recording and transcription
- Accurate speech-to-text conversion using Google Speech Recognition
- Support for various audio formats with automatic conversion

### 📝 **Comprehensive Assessment**
- **Accuracy Score**: How precisely you read the original text
- **Pronunciation Score**: Quality of pronunciation and articulation
- **Fluency Score**: Reading rhythm, pace, and natural flow
- **CEFR Level Assessment**: Automatic proficiency level determination

### 🎓 **Detailed Feedback System**
- Pronunciation error identification
- Missed words analysis
- Reading pace assessment (too fast/slow/appropriate)
- Personalized improvement recommendations
- Motivational comments and encouragement

## 🚀 Getting Started

### Try Online First
Before setting up locally, test the system using our **[Live Demo](https://huggingface.co/spaces/YoussefA7med/English_Helper_Reading)** to see if it meets your needs!

### Prerequisites

Before running the application locally, ensure you have the following:

- Python 3.8 or higher
- Required Python packages (see [Installation](#installation))
- API keys for the required services
- Microphone access for audio recording

### Required API Keys

You'll need to obtain the following API key:

1. **DeepSeek API Key**: For AI-powered content generation and evaluation
   - Sign up at [DeepSeek Platform](https://platform.deepseek.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/youssefa7med/english-reading-evaluation.git
   cd english-reading-evaluation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   ```

4. **Run the application**
   ```bash
   python reading_evaluation.py
   ```

5. **Access the interface**
   
   Open your browser and navigate to the URL displayed in the terminal (typically `http://localhost:7860`)

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
gradio>=4.0.0
requests>=2.31.0
python-dotenv>=1.0.0
pydub>=0.25.1
SpeechRecognition>=3.10.0
PyAudio>=0.2.11
```

## 🎮 How to Use

### Step 1: Enter Topic
- Input any topic you want to practice reading with
- Examples: "Climate Change", "Technology", "Travel", "History", "Science"

### Step 2: Generate Reading Passage
- Click "Generate Reading Passage" to create your personalized content
- The system generates a coherent passage with 4 paragraphs of increasing difficulty

### Step 3: Record Your Reading
- **Read the passage aloud**: Take your time to read clearly and naturally
- **Record your voice**: Use the built-in audio recorder
- **Practice multiple times**: Re-record until you're satisfied with your reading

### Step 4: Get Evaluated
- Click "Evaluate My Reading" to receive detailed feedback
- Get comprehensive analysis of your pronunciation, accuracy, and fluency
- Receive personalized recommendations for improvement

## 🏗️ System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Topic Input   │───▶│  Content Gen.    │───▶│ Reading Passage │
└─────────────────┘    │  (DeepSeek API)  │    │  (4 Levels)     │
                       └──────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Evaluation    │◀───│ Speech-to-Text   │◀───│ Audio Recording │
│   (DeepSeek)    │    │    (Google)      │    │   (Gradio)      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 🎯 Learning Benefits

### For Language Learners
- **Progressive Skill Building**: Start at your level and advance gradually
- **Pronunciation Improvement**: Get specific feedback on pronunciation errors
- **Fluency Development**: Practice natural reading rhythm and pace
- **Self-paced Learning**: Practice with unlimited topics and repetition

### For Educators
- **Assessment Tool**: Objectively evaluate student reading performance
- **Curriculum Support**: Generate materials for specific topics or levels
- **Progress Tracking**: Monitor improvement over time
- **CEFR Alignment**: Standards-based evaluation system

## 📊 Evaluation Metrics

### Core Scores
- **Accuracy Score (0-100)**: Measures how precisely you read the original text
- **Pronunciation Score (0-100)**: Evaluates articulation and phonetic accuracy
- **Fluency Score (0-100)**: Assesses reading rhythm and natural flow

### Detailed Analysis
- **Pronunciation Errors**: Specific sounds or words that need improvement
- **Missed Words**: Words from the original text that were skipped or mispronounced
- **Reading Pace**: Whether your reading speed is appropriate for comprehension
- **Strengths**: What you're doing well in your reading
- **Improvement Areas**: Specific skills that need development

## 🔧 Customization

### Adding New Difficulty Levels
Modify the `generate_reading_passage()` function to include additional CEFR levels or custom difficulty parameters.

### Changing Speech Recognition Settings
Update the `transcribe_audio()` function to use different languages or recognition services.

### Custom Evaluation Criteria
Extend the evaluation system by modifying the `evaluate_reading_performance()` function to include additional assessment metrics.

## 📊 Technical Details

### AI Models Used
- **Content Generation**: DeepSeek Chat API for creating graduated difficulty passages
- **Performance Evaluation**: Advanced language processing for comprehensive reading assessment
- **Speech Recognition**: Google Speech Recognition API for accurate transcription

### Supported Languages
- Primary: English (US)
- Speech recognition optimized for English pronunciation assessment

### Audio Processing
- **Input formats**: Various audio formats supported through PyDub
- **Output format**: WAV for optimal speech recognition
- **Quality**: Optimized for clear speech recognition and analysis

## 🤝 Contributing

We welcome contributions to improve the English Reading Evaluation System!

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution
- Additional language support
- New evaluation metrics
- UI/UX improvements
- Performance optimizations
- Offline speech recognition options

## 🐛 Troubleshooting

### Common Issues

**Issue: Microphone not working**
- Solution: Check browser permissions for microphone access
- Ensure PyAudio is properly installed for local deployment

**Issue: Speech recognition fails**
- Solution: Check internet connection (Google Speech Recognition requires internet)
- Speak clearly and at moderate pace

**Issue: Evaluation not working**
- Solution: Verify DeepSeek API key is valid and has sufficient credits

**Issue: Audio conversion errors**
- Solution: Ensure PyDub and ffmpeg are properly installed

### Getting Help
- Check the [Issues](https://github.com/youssefa7med/english-reading-evaluation/issues) page
- Create a new issue with detailed error descriptions
- Include system information and error logs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **DeepSeek**: For providing advanced language AI capabilities
- **Google Speech Recognition**: For accurate speech-to-text conversion
- **Gradio**: For the intuitive web interface framework
- **CEFR Framework**: For standardized language proficiency guidelines
- **PyDub**: For robust audio processing capabilities

## 📞 Contact

- **Project Maintainer**: [Youssef Ahmed](mailto:youssef111ahmed111@gmail.com)
- **GitHub**: [@youssefa7med](https://github.com/youssefa7med)

---

### 🌟 Star this repository if it helped you improve your English reading and pronunciation skills!

**Made with ❤️ for English language learners worldwide**
