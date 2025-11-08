### 🌟🌟🌟 Find interesting work or want your work to be on-board? Raise an Issue or Pull Requests! :)
## Contributors
We thank the following contributors for their valuable contributions!
[zwenyu](https://github.com/zwenyu), 
[Yuan-ManX](https://github.com/Yuan-ManX), 
[chaoweihuang](https://github.com/chaoweihuang), 
[Liu-Tianchi](https://github.com/Liu-Tianchi), 
[Sakshi113](https://github.com/Sakshi113), 
[hbwu-ntu](https://github.com/hbwu-ntu), 
[potsawee](https://github.com/potsawee), 
[czwxian](https://github.com/czwxian), 
[marianasignal](https://github.com/marianasignal), 
and You!
[![Star History Chart](https://api.star-history.com/svg?repos=AudioLLMs/Awesome-Audio-LLM&type=Date)](https://star-history.com/#AudioLLMs/Awesome-Audio-LLM&Date)
## Table of Contents
- [Dataset Resource](#dataset-resource)
- [Model and Methods](#model-and-methods)
- [Benchmark](#benchmark)
- [Survey](#survey)
- [Multimodal](#multimodal)
- [Study](#study)
- [Safety](#safety)
- [Chatbot](#chatbot)

<img src="model_release_timeline_vertical_listed.png" alt="Timeline Visualization" width="600">

### Abbreviations with Links
- [ACORN](https://arxiv.org/abs/2506.08524)
- [CMI-Bench](https://arxiv.org/abs/2506.12285)
- [PAL](https://arxiv.org/abs/2506.10423)
- [MMAR](https://arxiv.org/abs/2505.13032)
- [Audio-FLAN](https://arxiv.org/abs/2502.16584)
- [OSUM](https://arxiv.org/pdf/2501.13306)
- [Step-Audio](https://arxiv.org/abs/2502.11946)
- [Audio-CoT](https://arxiv.org/abs/2501.07246)
- [UltraEval-Audio](https://github.com/OpenBMB/UltraEval-Audio)
- [LUCY](https://arxiv.org/abs/2501.16327)
- [MinMo](https://arxiv.org/abs/2501.06282)
- [ADU-Bench](https://arxiv.org/abs/2412.05167)
- [TalkArena](https://talkarena.org/)
- [Typhoon2-Audio](https://arxiv.org/abs/2412.13702)
- [MERaLiON-AudioLLM](https://arxiv.org/abs/2412.09818)
- [ADU-Bench](https://arxiv.org/abs/2412.05167)
- [Taiwanese AudioLLM](https://arxiv.org/pdf/2411.07111)
- [WavChat-Survey](https://arxiv.org/abs/2411.13577)
- [Dynamic-SUPERB Phase-2](https://arxiv.org/pdf/2411.05361)
- [VoiceBench](https://arxiv.org/pdf/2410.17196)
- [MMAU](https://arxiv.org/pdf/2410.19168)
- [SPIRIT LM](https://arxiv.org/abs/2402.05755)
- [SpeechLLM-Survey](https://arxiv.org/pdf/2410.18908v2)
- [SpeechEmotionLlama](https://arxiv.org/pdf/2410.01162)
- [SPIRIT LM](https://arxiv.org/pdf/2402.05755)
- [SpeechLM-Survey](https://arxiv.org/pdf/2410.03751)
- [DiVA](https://arxiv.org/pdf/2410.02678)
- [AudioBERT](https://arxiv.org/pdf/2409.08199)
- [Ultravox](https://github.com/fixie-ai/ultravox)
- [LLaMA-Omni](https://arxiv.org/pdf/2409.06666v1)
- [SALMon](https://arxiv.org/abs/2409.07437)
- [DeSTA2](https://arxiv.org/pdf/2409.20007)
- [ASRCompare](https://arxiv.org/pdf/2409.00800v1)
- [MoWE-Audio](https://arxiv.org/pdf/2409.06635)
- [Moshi](https://arxiv.org/pdf/2410.00037)
- [EMOVA](https://arxiv.org/pdf/2409.18042)
- [MuChoMusic](https://arxiv.org/abs/2408.01337)
- [Mini-Omni](https://arxiv.org/pdf/2408.16725)
- [MooER](https://arxiv.org/pdf/2408.05101)
- [Typhoon-Audio](https://arxiv.org/abs/2409.10999)
- [Qwen2-Audio](https://arxiv.org/pdf/2407.10759)
- [LLaST](https://arxiv.org/pdf/2407.15415)
- [Decoder-only LLMs for STT](https://arxiv.org/pdf/2407.03169)
- [AudioEntailment](https://arxiv.org/pdf/2407.18062)
- [GAMA](https://arxiv.org/abs/2406.11768)
- [FunAudioLLM](https://arxiv.org/pdf/2407.04051v3)
- [CompA](https://arxiv.org/abs/2310.08753)
- [Speech ReaLLM](https://arxiv.org/pdf/2406.09569)
- [Audio Hallucination](https://arxiv.org/pdf/2406.08402)
- [AudioBench](https://arxiv.org/abs/2406.16020)
- [DeSTA](https://arxiv.org/abs/2406.18871)
- [CodecFake](https://arxiv.org/abs/2406.07237)
- [SD-Eval](https://arxiv.org/pdf/2406.13340)
- [MusiLingo](https://arxiv.org/pdf/2309.08730)
- [AIR-Bench](https://aclanthology.org/2024.acl-long.109/)
- [Audio Flamingo](https://arxiv.org/abs/2402.01831)
- [VoiceJailbreak](https://arxiv.org/pdf/2405.19103)
- [LibriSQA](https://arxiv.org/abs/2308.10390)
- [SALMONN](https://arxiv.org/pdf/2310.13289.pdf)
- [SpokenWOZ](https://arxiv.org/abs/2305.13040)
- [WavLLM](https://arxiv.org/pdf/2404.00656)
- [SLAM-LLM](https://arxiv.org/pdf/2402.08846)
- [AudioLM-Survey](https://arxiv.org/abs/2402.13236)
- [Pengi](https://arxiv.org/pdf/2305.11834.pdf)
- [Qwen-Audio](https://arxiv.org/pdf/2311.07919.pdf)
- [CoDi-2](https://arxiv.org/pdf/2311.18775)
- [UniAudio](https://arxiv.org/abs/2310.00704)
- [Dynamic-SUPERB](https://arxiv.org/abs/2309.09510)
- [LLaSM](https://arxiv.org/pdf/2308.15930.pdf)
- [Segment-level Q-Former](https://arxiv.org/pdf/2309.13963)
- [Prompting LLMs with Speech Recognition](https://arxiv.org/pdf/2307.11795)
- [Macaw-LLM](https://arxiv.org/pdf/2306.09093)
- [SpeechGPT](https://arxiv.org/pdf/2305.11000.pdf)
- [AudioGPT](https://arxiv.org/pdf/2304.12995.pdf)

## Dataset Resource

- `【2025-02】-【Audio-FLAN】-【The Hong Kong University of Science and Technology】-【Type: Dataset Resource】`
  - **Audio-FLAN: A Preliminary Release**
  - **Author(s):** Liumeng Xue, Ziya Zhou, Jiahao Pan, Zixuan Li, Shuai Fan, Yinghao Ma, Sitong Cheng, Dongchao Yang, Haohan Guo, Yujia Xiao, Xinsheng Wang, Zixuan Shen, Chuanbo Zhu, Xinshen Zhang, Tianchi Liu, Ruibin Yuan, Zeyue Tian, Haohe Liu, Emmanouil Benetos, Ge Zhang, Yike Guo, Wei Xue
  - [![GitHub stars](https://img.shields.io/github/stars/lmxue/Audio-FLAN?style=social)](https://github.com/lmxue/Audio-FLAN)
  - [Paper](https://arxiv.org/abs/2502.16584) / [Hugging Face Model](https://huggingface.co/datasets/HKUSTAudio/Audio-FLAN-Dataset)

- `【2024-04】-【LibriSQA】-【Shanghai Jiao Tong University】-【Type: Dataset Resource】`
  - **LibriSQA: A Novel Dataset and Framework for Spoken Question Answering with Large Language Models**
  - **Author(s):** Zihan Zhao, Yiyang Jiang, Heyang Liu, Yanfeng Wang, Yu Wang
  - [![GitHub stars](https://img.shields.io/github/stars/ZihanZhaoSJTU/LibriSQA?style=social)](https://github.com/ZihanZhaoSJTU/LibriSQA)
  - [Paper](https://arxiv.org/abs/2308.10390)

## Model and Methods

- `【2025-07】-【ACORN】-【NIO】-【Type: Model】`
  - **Teaching Physical Awareness to LLMs through Sounds**
  - **Author(s):** Weiguo Wang, Andy Nie, Wenrui Zhou, Yi Kai, Chengchen Hu
  - [Paper](https://arxiv.org/abs/2506.08524) / [Other Link](https://icml.cc/virtual/2025/poster/46139)

- `【2025-06】-【PAL】-【CVSSP,PAI@University of Surrey UK, MBZUAI Abu Dhabi】-【Type: Model】`
  - **PAL: Probing Audio Encoders via LLMs - A Study of Information Transfer from Audio Encoders to LLMs**
  - **Author(s):** Tony Alex, Wish Suharitdamrong, Sara Atito, Armin Mustafa, Philip J. B. Jackson, Imran Razzak, Muhammad Awais
  - [![GitHub stars](https://img.shields.io/github/stars/ta012/PAL-AudioLLM?style=social)](https://github.com/ta012/PAL-AudioLLM)
  - [Paper](https://arxiv.org/abs/2506.10423) / [Other Link](https://ta012.github.io/PAL/)

- `【2025-02】-【OSUM】-【ASLP@NPU】-【Type: Model】`
  - **OSUM: Advancing Open Speech Understanding Models with Limited Resources in Academia**
  - **Author(s):** Xuelong Geng, Kun Wei, Qijie Shao, Shuiyun Liu, Zhennan Lin, Zhixian Zhao, Guojian Li, Wenjie Tian, Peikun Chen, Yangze Li, Pengcheng Guo, Mingchen Shao, Shuiyuan Wang, Yuang Cao, Chengyou Wang, Tianyi Xu, Yuhang Dai, Xinfa Zhu, Yue Li, Li Zhang, Lei Xie
  - [![GitHub stars](https://img.shields.io/github/stars/ASLP-lab/OSUM?style=social)](https://github.com/ASLP-lab/OSUM)
  - [Paper](https://arxiv.org/pdf/2501.13306) / [Hugging Face Model](https://huggingface.co/spaces/ASLP-lab/OSUM)

- `【2025-02】-【Step-Audio】-【Step-Audio Team, StepFun】-【Type: Model】`
  - **Step-Audio: Unified Understanding and Generation in Intelligent Speech Interaction**
  - **Author(s):** Ailin Huang, Boyong Wu, Bruce Wang, Chao Yan, Chen Hu, Chengli Feng, Fei Tian, Feiyu Shen, Jingbei Li, Mingrui Chen, Peng Liu, Ruihang Miao, Wang You, Xi Chen, Xuerui Yang, Yechang Huang, Yuxiang Zhang, Zheng Gong, Zixin Zhang, Hongyu Zhou, Jianjian Sun, Brian Li, Chengting Feng, Changyi Wan, Hanpeng Hu, Jianchang Wu, Jiangjie Zhen, Ranchen Ming, Song Yuan, Xuelin Zhang, Yu Zhou, Bingxin Li, Buyun Ma, Hongyuan Wang, Kang An, Wei Ji, Wen Li, Xuan Wen, Xiangwen Kong, Yuankai Ma, Yuanwei Liang, Yun Mou, Bahtiyar Ahmidi, Bin Wang, Bo Li, Changxin Miao, Chen Xu, Chenrun Wang, Dapeng Shi, Deshan Sun, Dingyuan Hu, Dula Sai, Enle Liu, Guanzhe Huang, Gulin Yan, Heng Wang, Haonan Jia, Haoyang Zhang, Jiahao Gong, Junjing Guo, Jiashuai Liu, Jiahong Liu, Jie Feng, Jie Wu, Jiaoren Wu, Jie Yang, Jinguo Wang, Jingyang Zhang, Junzhe Lin, Kaixiang Li, Lei Xia, Li Zhou, Liang Zhao, Longlong Gu, Mei Chen, Menglin Wu, Ming Li, Mingxiao Li, Mingliang Li, Mingyao Liang, Na Wang, Nie Hao, Qiling Wu, Qinyuan Tan, Ran Sun, Shuai Shuai, Shaoliang Pang, Shiliang Yang, Shuli Gao, Shanshan Yuan, Siqi Liu, Shihong Deng, Shilei Jiang, Sitong Liu, Tiancheng Cao, Tianyu Wang, Wenjin Deng, Wuxun Xie, Weipeng Ming, Wenqing He , Wen Sun, Xin Han, Xin Huang, Xiaomin Deng, Xiaojia Liu, Xin Wu, Xu Zhao, Yanan Wei, Yanbo Yu, Yang Cao, Yangguang Li, Yangzhen Ma, Yanming Xu, Yaoyu Wang, Yaqiang Shi, Yilei Wang, Yizhuang Zhou, Yinmin Zhong, Yang Zhang, Yaoben Wei, Yu Luo, Yuanwei Lu, Yuhe Yin, Yuchu Luo, Yuanhao Ding, Yuting Yan, Yaqi Dai, Yuxiang Yang, Zhe Xie, Zheng Ge, Zheng Sun, Zhewei Huang, Zhichao Chang, Zhisheng Guan, Zidong Yang, Zili Zhang, Binxing Jiao, Daxin Jiang, Heung-Yeung Shum, Jiansheng Chen, Jing Li, Shuchang Zhou, Xiangyu Zhang, Xinhao Zhang, Yibo Zhu
  - [![GitHub stars](https://img.shields.io/github/stars/stepfun-ai/Step-Audio?style=social)](https://github.com/stepfun-ai/Step-Audio)
  - [Paper](https://arxiv.org/abs/2502.11946) / [Hugging Face Model](https://huggingface.co/stepfun-ai/Step-Audio-Chat)

- `【2025-01】-【Audio-CoT】-【Nanyang Technological University, Singapore】-【Type: Model】`
  - **Audio-CoT: Exploring Chain-of-Thought Reasoning in Large Audio Language Model**
  - **Author(s):** Ziyang Ma, Zhuo Chen, Yuping Wang, Eng Siong Chng, Xie Chen
  - [Paper](https://arxiv.org/abs/2501.07246)

- `【2025-01】-【LUCY】-【Tencent】-【Type: Model】`
  - **LUCY: Linguistic Understanding and Control Yielding Early Stage of Her**
  - **Author(s):** Heting Gao, Hang Shao, Xiong Wang, Chaofan Qiu, Yunhang Shen, Siqi Cai, Yuchen Shi, Zihan Xu, Zuwei Long, Yike Zhang, Shaoqi Dong, Chaoyou Fu, Ke Li, Long Ma, Xing Sun
  - [![GitHub stars](https://img.shields.io/github/stars/VITA-MLLM/LUCY?style=social)](https://github.com/VITA-MLLM/LUCY)
  - [Paper](https://arxiv.org/abs/2501.16327)

- `【2024-12】-【Typhoon2-Audio】-【SCB 10X】-【Type: Multimodal Language Model】`
  - **Typhoon2-Audio: A Thai Multimodal Language Model for Speech and Text Processing**
  - **Author(s):** Kunat Pipatanakul, Potsawee Manakul, Natapong Nitarach, Warit Sirichotedumrong, Surapon Nonesung, Teetouch Jaknamon, Parinthapat Pengpun, Pittawat Taveekitworachai, Adisai Na-Thalang, Sittipong Sripaisarnmongkol, Krisanapong Jirayoot, Kasima Tharnpipitchai
  - [![GitHub stars](https://img.shields.io/github/stars/typhoon2-audio/?style=social)](https://github.com/scb-10x/typhoon2-audio/)
  - [Paper](https://arxiv.org/abs/2412.13702) / [Hugging Face Model](https://huggingface.co/scb10x/llama3.1-typhoon2-audio-8b-instruct) / [Demo](https://audio.opentyphoon.ai/)

- `【2024-12】-【MERaLiON-AudioLLM】-【I2R, A*STAR, Singapore】-【Type: Model】`
  - **MERaLiON-AudioLLM: Bridging Audio and Language with Large Language Models**
  - **Author(s):** Yingxu He, Zhuohan Liu, Shuo Sun, Bin Wang, Wenyu Zhang, Xunlong Zou, Nancy F. Chen, Ai Ti Aw
  - [Paper](https://arxiv.org/abs/2412.09818) / [Hugging Face Model](https://huggingface.co/MERaLiON/MERaLiON-AudioLLM-Whisper-SEA-LION) / [Demo](https://huggingface.co/spaces/MERaLiON/MERaLiON-AudioLLM)

- `【2024-11】-【Taiwanese AudioLLM】-【National Taiwan University】-【Type: Model】`
  - **Building a Taiwanese Mandarin Spoken Language Model: A First Attempt**
  - **Author(s):** Chih-Kai Yang, Yu-Kuan Fu, Chen-An Li, Yi-Cheng Lin, Yu-Xiang Lin, Wei-Chih Chen, Ho Lam Chung, Chun-Yi Kuan, Wei-Ping Huang, Ke-Han Lu, Tzu-Quan Lin, Hsiu-Hsuan Wang, En-Pei Hu, Chan-Jan Hsu, Liang-Hsuan Tseng, I-Hsiang Chiu, Ulin Sanga, Xuanjun Chen, Po-chun Hsu, Shu-wen Yang, Hung-yi Lee
  - [Paper](https://arxiv.org/pdf/2411.07111)

- `【2024-10】-【SPIRIT LM】-【Meta】-【Type: Model】`
  - **SPIRIT LM: Interleaved Spoken and Written Language Model**
  - **Author(s):** Tu Anh Nguyen, Benjamin Muller, Bokai Yu, Marta R. Costa-jussa, Maha Elbayad, Sravya Popuri, Christophe Ropers, Paul-Ambroise Duquenne, Robin Algayres, Ruslan Mavlyutov, Itai Gat, Mary Williamson, Gabriel Synnaeve, Juan Pino, Benoit Sagot, Emmanuel Dupoux
  - [![GitHub stars](https://img.shields.io/github/stars/facebookresearch/spiritlm?style=social)](https://github.com/facebookresearch/spiritlm)
  - [Paper](https://arxiv.org/abs/2402.05755) / [Other Link](https://speechbot.github.io/spiritlm/)

- `【2024-10】-【SpeechEmotionLlama】-【MIT, Meta】-【Type: Model】`
  - **Frozen Large Language Models Can Perceive Paralinguistic Aspects of Speech**
  - **Author(s):** Wonjune Kang, Junteng Jia, Chunyang Wu, Wei Zhou, Egor Lakomkin, Yashesh Gaur, Leda Sari, Suyoun Kim, Ke Li, Jay Mahadeokar, Ozlem Kalinli
  - [Paper](https://arxiv.org/pdf/2410.01162)

- `【2024-10】-【SPIRIT LM】-【Meta】-【Type: Model】`
  - **SPIRIT LM: Interleaved Spoken and Written Language Model**
  - **Author(s):** Tu Anh Nguyen, Benjamin Muller, Bokai Yu, Marta R. Costa-jussa, Maha Elbayad, Sravya Popuri, Paul-Ambroise Duquenne, Robin Algayres, Ruslan Mavlyutov, Itai Gat, Gabriel Synnaeve, Juan Pino, Benoît Sagot, Emmanuel Dupoux
  - [![GitHub stars](https://img.shields.io/github/stars/facebookresearch/spiritlm?style=social)](https://github.com/facebookresearch/spiritlm)
  - [Paper](https://arxiv.org/pdf/2402.05755) / [Demo](https://speechbot.github.io/spiritlm/)

- `【2024-10】-【DiVA】-【Georgia Tech, Stanford】-【Type: Model】`
  - **Distilling an End-to-End Voice Assistant Without Instruction Training Data**
  - **Author(s):** William Held, Ella Li, Michael Ryan, Weiyan Shi, Yanzhe Zhang, Diyi Yang
  - [![GitHub stars](https://img.shields.io/github/stars/github.com/diva-audio?style=social)](https://github.com/diva-audio)
  - [Paper](https://arxiv.org/pdf/2410.02678) / [Demo](https://diva-audio.github.io/)

- `【2024-09】-【AudioBERT】-【POSTECH, Inha University】-【Type: Model】`
  - **AudioBERT: Audio Knowledge Augmented Language Model**
  - **Author(s):** Hyunjong Ok, Suho Yoo, Jaeho Lee
  - [![GitHub stars](https://img.shields.io/github/stars/HJ-Ok/AudioBERT?style=social)](https://github.com/HJ-Ok/AudioBERT)
  - [Paper](https://arxiv.org/pdf/2409.08199)

- `【2024-09】-【Ultravox】-【Fixie.ai】-【Type: Model】`
  - **Ultravox: A Fast Multimodal LLM for Real-Time Voice**
  - **Author(s):** 
  - [![GitHub stars](https://img.shields.io/github/stars/fixie-ai/ultravox?style=social)](https://github.com/fixie-ai/ultravox)

- `【2024-09】-【LLaMA-Omni】-【Institute of Computing Technology, Chinese Academy of Sciences (ICT/CAS)】-【Type: Model】`
  - **LLaMA-Omni: Seamless Speech Interaction with Large Language Models**
  - **Author(s):** Qingkai Fang, Shoutao Guo, Yan Zhou, Zhengrui Ma, Shaolei Zhang, Yang Feng
  - [![GitHub stars](https://img.shields.io/github/stars/ictnlp/llama-omni?style=social)](https://github.com/ictnlp/llama-omni)
  - [Paper](https://arxiv.org/pdf/2409.06666v1)

- `【2024-09】-【DeSTA2】-【National Taiwan University, NVIDIA】-【Type: Model】`
  - **Developing Instruction-Following Speech Language Model Without Speech Instruction-Tuning Data**
  - **Author(s):** Ke-Han Lu, Zhehuai Chen, Szu-Wei Fu, Chao-Han Huck Yang, Jagadeesh Balam, Boris Ginsburg, Yu-Chiang Frank Wang, Hung-yi Lee
  - [![GitHub stars](https://img.shields.io/github/stars/kehanlu/DeSTA2?style=social)](https://github.com/kehanlu/DeSTA2)
  - [Paper](https://arxiv.org/pdf/2409.20007)

- `【2024-09】-【ASRCompare】-【Tsinghua University, Tencent AI Lab】-【Type: Model】`
  - **Comparing Discrete and Continuous Space LLMs for Speech Recognition**
  - **Author(s):** Yaoxun Xu, Shi-Xiong Zhang, Jianwei Yu, Zhiyong Wu, Dong Yu
  - [![GitHub stars](https://img.shields.io/github/stars/xuyaoxun/ASRCompare?style=social)](https://github.com/xuyaoxun/ASRCompare)
  - [Paper](https://arxiv.org/pdf/2409.00800v1)

- `【2024-09】-【MoWE-Audio】-【A*STAR】-【Type: Model】`
  - **MoWE-Audio: Multitask AudioLLMs with Mixture of Weak Encoders**
  - **Author(s):** Wenyu Zhang, Shuo Sun, Bin Wang, Xunlong Zou, Zhuohan Liu, Yingxu He, Geyu Lin, Nancy F. Chen, Ai Ti Aw
  - [Paper](https://arxiv.org/pdf/2409.06635)

- `【2024-09】-【Moshi】-【Kyutai】-【Type: Model】`
  - **Moshi: a speech-text foundation model for real-time dialogue**
  - **Author(s):** Alexandre Défossez, Laurent Mazaré, Manu Orsini, Amélie Royer, Patrick Pérez, Hervé Jégou, Edouard Grave, Neil Zeghidour
  - [![GitHub stars](https://img.shields.io/github/stars/kyutai-labs/moshi?style=social)](https://github.com/kyutai-labs/moshi)
  - [Paper](https://arxiv.org/pdf/2410.00037)

- `【2024-08】-【Mini-Omni】-【Tsinghua University】-【Type: Model】`
  - **Mini-Omni: Language Models Can Hear, Talk While Thinking in Streaming**
  - **Author(s):** Zhifei Xie, Changqiao Wu
  - [![GitHub stars](https://img.shields.io/github/stars/gpt-omni/mini-omni?style=social)](https://github.com/gpt-omni/mini-omni)
  - [Paper](https://arxiv.org/pdf/2408.16725)

- `【2024-08】-【MooER】-【Moore Threads】-【Type: Model】`
  - **MooER: LLM-based Speech Recognition and Translation Models from Moore Threads**
  - **Author(s):** Zhenlin Liang, Junhao Xu, Yi Liu, Yichao Hu, Jian Li, Yajun Zheng, Meng Cai, Hua Wang
  - [![GitHub stars](https://img.shields.io/github/stars/MooreThreads/MooER?style=social)](https://github.com/MooreThreads/MooER)
  - [Paper](https://arxiv.org/pdf/2408.05101)

- `【2024-08】-【Typhoon-Audio】-【SCB 10X】-【Type: Multimodal Language Model】`
  - **Typhoon-Audio: Enhancing Low-Resource Language and Instruction Following Capabilities of Audio Language Models**
  - **Author(s):** Potsawee Manakul, Guangzhi Sun, Warit Sirichotedumrong, Kasima Tharnpipitchai, Kunat Pipatanakul
  - [Paper](https://arxiv.org/abs/2409.10999) / [Hugging Face Model](https://huggingface.co/scb10x/llama-3-typhoon-v1.5-8b-audio-preview)

- `【2024-07】-【Qwen2-Audio】-【Alibaba Group】-【Type: Model】`
  - **Qwen2-Audio Technical Report**
  - **Author(s):** Yunfei Chu, Jin Xu, Qian Yang, Haojie Wei, Xipin Wei, Zhifang Guo, Yichong Leng, Yuanjun Lv, Jinzheng He, Junyang Lin, Chang Zhou, Jingren Zhou
  - [![GitHub stars](https://img.shields.io/github/stars/QwenLM/Qwen2-Audio?style=social)](https://github.com/QwenLM/Qwen2-Audio)
  - [Paper](https://arxiv.org/pdf/2407.10759)

- `【2024-07】-【LLaST】-【The Chinese University of Hong Kong, Shenzhen; Shanghai AI Laboratory; Nara Institute of Science and Technology, Japan】-【Type: Model】`
  - **LLaST: Improved End-to-end Speech Translation System Leveraged by Large Language Models**
  - **Author(s):** Xi Chen, Songyang Zhang, Qibing Bai, Kai Chen, Satoshi Nakamura
  - [![GitHub stars](https://img.shields.io/github/stars/openaudiolab/LLaST?style=social)](https://github.com/openaudiolab/LLaST)
  - [Paper](https://arxiv.org/pdf/2407.15415)

- `【2024-07】-【Decoder-only LLMs for STT】-【NTU-Taiwan, Meta】-【Type: Research】`
  - **Investigating Decoder-only Large Language Models for Speech-to-text Translation**
  - **Author(s):** Authors not specified in the provided information
  - [Paper](https://arxiv.org/pdf/2407.03169)

- `【2024-07】-【GAMA】-【University of Maryland, College Park】-【Type: Model】`
  - **GAMA: A Large Audio-Language Model with Advanced Audio Understanding and Complex Reasoning Abilities**
  - **Author(s):** Sreyan Ghosh, Sonal Kumar, Ashish Seth, Chandra Kiran Reddy Evuru, Utkarsh Tyagi, S Sakshi, Oriol Nieto, Ramani Duraiswami, Dinesh Manocha
  - [![GitHub stars](https://img.shields.io/github/stars/Sreyan88/GAMA?style=social)](https://github.com/Sreyan88/GAMA)
  - [Paper](https://arxiv.org/abs/2406.11768) / [Demo](https://sreyan88.github.io/gamaaudio/)

- `【2024-07】-【FunAudioLLM】-【Alibaba】-【Type: Model】`
  - **FunAudioLLM: Voice Understanding and Generation Foundation Models for Natural Interaction Between Humans and LLMs**
  - **Author(s):** Authors not specified in the provided information
  - [![GitHub stars](https://img.shields.io/github/stars/github.com/FunAudioLLM?style=social)](https://github.com/FunAudioLLM)
  - [Paper](https://arxiv.org/pdf/2407.04051v3) / [Demo](https://fun-audio-llm.github.io/)

- `【2024-07】-【CompA】-【University of Maryland, College Park; Adobe, USA; NVIDIA, Bangalore, India】-【Type: Model】`
  - **CompA: Addressing the Gap in Compositional Reasoning in Audio-Language Models**
  - **Author(s):** Sreyan Ghosh, Ashish Seth, Sonal Kumar, Utkarsh Tyagi, Chandra Kiran Evuru, S. Ramaneswaran, S. Sakshi, Oriol Nieto, Ramani Duraiswami, Dinesh Manocha
  - [![GitHub stars](https://img.shields.io/github/stars/Sreyan88/CompA?style=social)](https://github.com/Sreyan88/CompA)
  - [Paper](https://arxiv.org/abs/2310.08753) / [Demo](https://sreyan88.github.io/compa_iclr/)

- `【2024-06】-【Speech ReaLLM】-【Meta】-【Type: Model】`
  - **Speech ReaLLM – Real-time Streaming Speech Recognition with Multimodal LLMs by Teaching the Flow of Time**
  - **Author(s):** Authors not specified in the provided information
  - [Paper](https://arxiv.org/pdf/2406.09569)

- `【2024-06】-【DeSTA】-【NTU-Taiwan, Nvidia】-【Type: Model】`
  - **DeSTA: Enhancing Speech Language Models through Descriptive Speech-Text Alignment**
  - **Author(s):** Authors not specified in the provided information
  - [![GitHub stars](https://img.shields.io/github/stars/multimodal/DeSTA?style=social)](https://github.com/kehanlu/Nemo/tree/desta/examples/multimodal/DeSTA)
  - [Paper](https://arxiv.org/abs/2406.18871)

- `【2024-06】-【MusiLingo】-【University of Pennsylvania】-【Type: Model】`
  - **MusiLingo: Bridging Music and Text with Pre-trained Language Models for Music Captioning and Query Response**
  - **Author(s):** Zihao Deng, Yinghao Ma, Yudong Liu, Rongchen Guo, Ge Zhang, Wenhu Chen, Wenhao Huang, Emmanouil Benetos
  - [![GitHub stars](https://img.shields.io/github/stars/zihaod/MusiLingo?style=social)](https://github.com/zihaod/MusiLingo)
  - [Paper](https://arxiv.org/pdf/2309.08730)

- `【2024-05】-【Audio Flamingo】-【Nvidia】-【Type: Model】`
  - **Audio Flamingo: A Novel Audio Language Model with Few-Shot Learning and Dialogue Abilities**
  - **Author(s):** Authors not specified in the provided information
  - [![GitHub stars](https://img.shields.io/github/stars/NVIDIA/audio-flamingo?style=social)](https://github.com/NVIDIA/audio-flamingo)
  - [Paper](https://arxiv.org/abs/2402.01831)

- `【2024-04】-【SALMONN】-【Tsinghua】-【Type: Model】`
  - **SALMONN: Towards Generic Hearing Abilities for Large Language Models**
  - **Author(s):** Authors not specified in the provided information
  - [![GitHub stars](https://img.shields.io/github/stars/bytedance/SALMONN?style=social)](https://github.com/bytedance/SALMONN)
  - [Paper](https://arxiv.org/pdf/2310.13289.pdf) / [Demo](https://huggingface.co/spaces/tsinghua-ee/SALMONN-7B-gradio)

- `【2024-03】-【WavLLM】-【CUHK】-【Type: Model】`
  - **WavLLM: Towards Robust and Adaptive Speech Large Language Model**
  - **Author(s):** Authors not specified in the provided information
  - [![GitHub stars](https://img.shields.io/github/stars/main/WavLLM?style=social)](https://github.com/microsoft/SpeechT5/tree/main/WavLLM)
  - [Paper](https://arxiv.org/pdf/2404.00656)

- `【2024-02】-【SLAM-LLM】-【Shanghai Jiao Tong University (SJTU)】-【Type: Model】`
  - **An Embarrassingly Simple Approach for LLM with Strong ASR Capacity**
  - **Author(s):** Authors not specified in the provided information
  - [![GitHub stars](https://img.shields.io/github/stars/X-LANCE/SLAM-LLM?style=social)](https://github.com/X-LANCE/SLAM-LLM)
  - [Paper](https://arxiv.org/pdf/2402.08846)

- `【2024-01】-【Pengi】-【Microsoft】-【Type: Model】`
  - **Pengi: An Audio Language Model for Audio Tasks**
  - **Author(s):** Authors not specified in the provided information
  - [![GitHub stars](https://img.shields.io/github/stars/microsoft/Pengi?style=social)](https://github.com/microsoft/Pengi)
  - [Paper](https://arxiv.org/pdf/2305.11834.pdf)

- `【2023-12】-【Qwen-Audio】-【Alibaba】-【Type: Model】`
  - **Qwen-Audio: Advancing Universal Audio Understanding via Unified Large-Scale Audio-Language Models**
  - **Author(s):** Authors not specified in the provided information
  - [![GitHub stars](https://img.shields.io/github/stars/QwenLM/Qwen-Audio?style=social)](https://github.com/QwenLM/Qwen-Audio)
  - [Paper](https://arxiv.org/pdf/2311.07919.pdf) / [Demo](https://qwen-audio.github.io/Qwen-Audio/)

- `【2023-10】-【UniAudio】-【Chinese University of Hong Kong (CUHK)】-【Type: Model】`
  - **An Audio Foundation Model Toward Universal Audio Generation**
  - **Author(s):** Authors not specified in the provided information
  - [![GitHub stars](https://img.shields.io/github/stars/yangdongchao/UniAudio?style=social)](https://github.com/yangdongchao/UniAudio)
  - [Paper](https://arxiv.org/abs/2310.00704) / [Demo](https://dongchaoyang.top/UniAudio_demo/)

- `【2023-09】-【LLaSM】-【LinkSoul.AI】-【Type: Model】`
  - **LLaSM: Large Language and Speech Model**
  - **Author(s):** Authors not specified in the provided information
  - [![GitHub stars](https://img.shields.io/github/stars/LinkSoul-AI/LLaSM?style=social)](https://github.com/LinkSoul-AI/LLaSM)
  - [Paper](https://arxiv.org/pdf/2308.15930.pdf)

- `【2023-09】-【Segment-level Q-Former】-【Tsinghua University, ByteDance】-【Type: Model】`
  - **Connecting Speech Encoder and Large Language Model for ASR**
  - **Author(s):** Wenyi Yu, Changli Tang, Guangzhi Sun, Xianzhao Chen, Tian Tan, Wei Li, Lu Lu, Zejun Ma, Chao Zhang
  - [Paper](https://arxiv.org/pdf/2309.13963)

- `【2023-07】-【Prompting LLMs with Speech Recognition】-【Meta】-【Type: Model】`
  - **Prompting Large Language Models with Speech Recognition Abilities**
  - **Author(s):** Yassir Fathullah, Chunyang Wu, Egor Lakomkin, Junteng Jia, Yuan Shangguan, Ke Li, Jinxi Guo, Wenhan Xiong, Jay Mahadeokar, Ozlem Kalinli, Christian Fuegen, Mike Seltzer
  - [Paper](https://arxiv.org/pdf/2307.11795)

- `【2023-05】-【SpeechGPT】-【Fudan University】-【Type: Model】`
  - **SpeechGPT: Empowering Large Language Models with Intrinsic Cross-Modal Conversational Abilities**
  - **Author(s):** Dong Zhang, Shimin Li, Xin Zhang, Jun Zhan, Pengyu Wang, Yaqian Zhou, Xipeng Qiu
  - [![GitHub stars](https://img.shields.io/github/stars/main/speechgpt?style=social)](https://github.com/0nutation/SpeechGPT/tree/main/speechgpt)
  - [Paper](https://arxiv.org/pdf/2305.11000.pdf) / [Demo](https://0nutation.github.io/SpeechGPT.github.io/)

- `【2023-04】-【AudioGPT】-【Zhejiang University】-【Type: Model】`
  - **AudioGPT: Understanding and Generating Speech, Music, Sound, and Talking Head**
  - **Author(s):** Rongjie Huang, Mingze Li, Dongchao Yang, Jiatong Shi, Xuankai Chang, Zhenhui Ye, Yuning Wu, Zhiqing Hong, Jiawei Huang, Jinglin Liu, Yi Ren, Zhou Zhao, Shinji Watanabe
  - [![GitHub stars](https://img.shields.io/github/stars/AIGC-Audio/AudioGPT?style=social)](https://github.com/AIGC-Audio/AudioGPT)
  - [Paper](https://arxiv.org/pdf/2304.12995.pdf)

## Benchmark

- `【2025-06】-【CMI-Bench】-【Queen Mary University of London】-【Type: Benchmark】`
  - **CMI-Bench: A Comprehensive Benchmark for Evaluating Music Instruction Following**
  - **Author(s):** Yinghao Ma, Siyou Li, Juntao Yu, Emmanouil Benetos, Akira Maezawa
  - [![GitHub stars](https://img.shields.io/github/stars/nicolaus625/CMI-bench?style=social)](https://github.com/nicolaus625/CMI-bench)
  - [Paper](https://arxiv.org/abs/2506.12285) / [Hugging Face Model](https://huggingface.co/papers/2506.12285)

- `【2025-05】-【MMAR】-【Shanghai Jiao Tong University】-【Type: Benchmark】`
  - **MMAR: A Challenging Benchmark for Deep Reasoning in Speech, Audio, Music, and Their Mix**
  - **Author(s):** Ziyang Ma, Yinghao Ma, Yanqiao Zhu, Chen Yang, Yi-Wen Chao, Ruiyang Xu, Wenxi Chen, Yuanzhe Chen, Zhuo Chen, Jian Cong, Kai Li, Keliang Li, Siyou Li, Xinfeng Li, Xiquan Li, Zheng Lian, Yuzhe Liang, Minghao Liu, Zhikang Niu, Tianrui Wang, Yuping Wang, Yuxuan Wang, Yihao Wu, Guanrou Yang, Jianwei Yu, Ruibin Yuan, Zhisheng Zheng, Ziya Zhou, Haina Zhu, Wei Xue, Emmanouil Benetos, Kai Yu, Eng-Siong Chng, Xie Chen
  - [Paper](https://arxiv.org/abs/2505.13032)

- `【2025-01】-【UltraEval-Audio】-【OpenBMB】-【Type: Benchmark】`
  - **UltraEval-Audio**
  - **Author(s):** OpenBMB
  - [![GitHub stars](https://img.shields.io/github/stars/OpenBMB/UltraEval-Audio?style=social)](https://github.com/OpenBMB/UltraEval-Audio)

- `【2024-12】-【ADU-Bench】-【Tsinghua University, University of Oxford】-【Type: Benchmark】`
  - **Benchmarking Open-ended Audio Dialogue Understanding for Large Audio-Language Models**
  - **Author(s):** Kuofeng Gao, Shu-Tao Xia, Ke Xu, Philip Torr, Jindong Gu
  - [Paper](https://arxiv.org/abs/2412.05167)

- `【2024-12】-【TalkArena】-【Stanford University, SCB 10X】-【Type: Interactive Benchmarking Tool】`
  - **TalkArena: Interactive Evaluation of Large Audio Models**
  - **Author(s):** Ella Minzhi Li*, Will Held*, Michael J. Ryan, Kunat Pipatanakul, Potsawee Manakul, Hao Zhu, Diyi Yang (*Equal Contribution)
  - [![GitHub stars](https://img.shields.io/github/stars/SALT-NLP/talk-arena?style=social)](https://github.com/SALT-NLP/talk-arena)
  - [Demo](https://talkarena.org/) / [Other Link](https://talkarena.org/blog)

- `【2024-12】-【ADU-Bench】-【Tsinghua University, University of Oxford】-【Type: Benchmark】`
  - **Benchmarking Open-ended Audio Dialogue Understanding for Large Audio-Language Models**
  - **Author(s):** Kuofeng Gao, Shu-Tao Xia, Ke Xu, Philip Torr, Jindong Gu
  - [Paper](https://arxiv.org/abs/2412.05167)

- `【2024-11】-【Dynamic-SUPERB Phase-2】-【National Taiwan University, University of Texas at Austin, Carnegie Mellon University, Nanyang Technological University, Toyota Technological Institute of Chicago, Université du Québec (INRS-EMT), NVIDIA, ASAPP, Renmin University of China】-【Type: Evaluation Framework】`
  - **Dynamic-SUPERB Phase-2: A Collaboratively Expanding Benchmark for Measuring the Capabilities of Spoken Language Models with 180 Tasks**
  - **Author(s):** Chien-yu Huang, Wei-Chih Chen, Shu-wen Yang, Andy T. Liu, Chen-An Li, Yu-Xiang Lin, Wei-Cheng Tseng, Anuj Diwan, Yi-Jen Shih, Jiatong Shi, William Chen, Xuanjun Chen, Chi-Yuan Hsiao, Puyuan Peng, Shih-Heng Wang, Chun-Yi Kuan, Haibin Wu, Siddhant Arora, Kai-Wei Chang, Yifan Peng, Roshan Sharma, Shinji Watanabe, Bhiksha Ramakrishnan, Shady Shehata, Hung-yi Lee
  - [![GitHub stars](https://img.shields.io/github/stars/dynamic-superb/dynamic-superb?style=social)](https://github.com/dynamic-superb/dynamic-superb)
  - [Paper](https://arxiv.org/pdf/2411.05361) / [Other Link](https://dynamic-superb.github.io/)

- `【2024-10】-【VoiceBench】-【National University of Singapore】-【Type: Benchmark】`
  - **VoiceBench: Benchmarking LLM-Based Voice Assistants**
  - **Author(s):** Yiming Chen, Xianghu Yue, Chen Zhang, Xiaoxue Gao, Robby T. Tan, Haizhou Li
  - [![GitHub stars](https://img.shields.io/github/stars/MatthewCYM/VoiceBench?style=social)](https://github.com/MatthewCYM/VoiceBench)
  - [Paper](https://arxiv.org/pdf/2410.17196)

- `【2024-10】-【MMAU】-【University of Maryland】-【Type: Benchmark】`
  - **MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark**
  - **Author(s):** S Sakshi, Utkarsh Tyagi, Sonal Kumar, Ashish Seth, Ramaneswaran Selvakumar, Oriol Nieto, Ramani Duraiswami, Sreyan Ghosh, Dinesh Manocha
  - [![GitHub stars](https://img.shields.io/github/stars/tree/main?style=social)](https://github.com/Sakshi113/mmau/tree/main)
  - [Paper](https://arxiv.org/pdf/2410.19168) / [Other Link](https://sakshi113.github.io/mmau_homepage/)

- `【2024-09】-【SALMon】-【Hebrew University of Jerusalem】-【Type: Benchmark】`
  - **A Suite for Acoustic Language Model Evaluation**
  - **Author(s):** Gallil Maimon, Amit Roth, Yossi Adi
  - [![GitHub stars](https://img.shields.io/github/stars/adiyoss-lab/salmon?style=social)](https://github.com/adiyoss-lab/salmon)
  - [Paper](https://arxiv.org/abs/2409.07437) / [Demo](https://pages.cs.huji.ac.il/adiyoss-lab/salmon/)

- `【2024-08】-【MuChoMusic】-【UPF, QMUL, UMG】-【Type: Benchmark】`
  - **MuChoMusic: Evaluating Music Understanding in Multimodal Audio-Language Models**
  - **Author(s):** Benno Weck, Ilaria Manco, Emmanouil Benetos, Elio Quinton, George Fazekas, Dmitry Bogdanov
  - [![GitHub stars](https://img.shields.io/github/stars/mulab-mir/muchomusic?style=social)](https://github.com/mulab-mir/muchomusic)
  - [Paper](https://arxiv.org/abs/2408.01337)

- `【2024-07】-【AudioEntailment】-【CMU, Microsoft】-【Type: Benchmark】`
  - **Audio Entailment: Assessing Deductive Reasoning for Audio Understanding**
  - **Author(s):** Soham Deshmukh, Shuo Han, Hazim Bukhari, Benjamin Elizalde, Hannes Gamper, Rita Singh, Bhiksha Raj
  - [![GitHub stars](https://img.shields.io/github/stars/microsoft/AudioEntailment?style=social)](https://github.com/microsoft/AudioEntailment)
  - [Paper](https://arxiv.org/pdf/2407.18062)

- `【2024-06】-【AudioBench】-【A*STAR, Singapore】-【Type: Benchmark】`
  - **AudioBench: A Universal Benchmark for Audio Large Language Models**
  - **Author(s):** Bin Wang, Xunlong Zou, Geyu Lin, Shuo Sun, Zhuohan Liu, Wenyu Zhang, Zhengyuan Liu, AiTi Aw, Nancy F. Chen
  - [![GitHub stars](https://img.shields.io/github/stars/AudioLLMs/AudioBench?style=social)](https://github.com/AudioLLMs/AudioBench)
  - [Paper](https://arxiv.org/abs/2406.16020) / [Demo](https://huggingface.co/spaces/AudioLLMs/AudioBench-Leaderboard)

- `【2024-06】-【SD-Eval】-【CUHK, Bytedance】-【Type: Benchmark】`
  - **SD-Eval: A Benchmark Dataset for Spoken Dialogue Understanding Beyond Words**
  - **Author(s):** Junyi Ao, Yuancheng Wang, Xiaohai Tian, Dekun Chen, Jun Zhang, Lu Lu, Yuxuan Wang, Haizhou Li, Zhizheng Wu
  - [![GitHub stars](https://img.shields.io/github/stars/amphionspace/SD-Eval?style=social)](https://github.com/amphionspace/SD-Eval)
  - [Paper](https://arxiv.org/pdf/2406.13340)

- `【2024-05】-【AIR-Bench】-【ZJU, Alibaba】-【Type: Benchmark】`
  - **AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension**
  - **Author(s):** Qian Yang, Jin Xu, Wenrui Liu, Yunfei Chu, Ziyue Jiang, Xiaohuan Zhou, Yichong Leng, Yuanjun Lv, Zhou Zhao, Chang Zhou, Jingren Zhou
  - [![GitHub stars](https://img.shields.io/github/stars/OFA-Sys/AIR-Bench?style=social)](https://github.com/OFA-Sys/AIR-Bench)
  - [Paper](https://aclanthology.org/2024.acl-long.109/)

- `【2024-03】-【SpokenWOZ】-【Tencent】-【Type: Benchmark】`
  - **SpokenWOZ: A Large-Scale Speech-Text Benchmark for Spoken Task-Oriented Dialogue Agents**
  - **Author(s):** Shuzheng Si, Wentao Ma, Haoyu Gao, Yuchuan Wu, Ting-En Lin, Yinpei Dai, Hangyu Li, Rui Yan, Fei Huang, Yongbin Li
  - [![GitHub stars](https://img.shields.io/github/stars/main/spokenwoz?style=social)](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/spokenwoz)
  - [Paper](https://arxiv.org/abs/2305.13040) / [Demo](https://spokenwoz.github.io/)

- `【2023-09】-【Dynamic-SUPERB】-【NTU-Taiwan, etc.】-【Type: Benchmark】`
  - **Dynamic-SUPERB: Towards A Dynamic, Collaborative, and Comprehensive Instruction-Tuning Benchmark for Speech**
  - **Author(s):** Chien-yu Huang, Ke-Han Lu, Shih-Heng Wang, Chi-Yuan Hsiao, Chun-Yi Kuan, Haibin Wu, Siddhant Arora, Kai-Wei Chang, Jiatong Shi, Yifan Peng, Roshan Sharma, Shinji Watanabe, Bhiksha Ramakrishnan, Shady Shehata, Hung-yi Lee
  - [![GitHub stars](https://img.shields.io/github/stars/dynamic-superb/dynamic-superb?style=social)](https://github.com/dynamic-superb/dynamic-superb)
  - [Paper](https://arxiv.org/abs/2309.09510)

## Survey

- `【2024-11】-【WavChat-Survey】-【Zhejiang University】-【Type: Survey】`
  - **WavChat: A Survey of Spoken Dialogue Models**
  - **Author(s):** Shengpeng Ji, Yifu Chen, Minghui Fang, Jialong Zuo, Jingyu Lu, Hanting Wang, Ziyue Jiang, Long Zhou, Shujie Liu, Xize Cheng, Xiaoda Yang, Zehan Wang, Qian Yang, Jian Li, Yidi Jiang, Jingzhen He, Yunfei Chu, Jin Xu, Zhou Zhao
  - [Paper](https://arxiv.org/abs/2411.13577)

- `【2024-10】-【SpeechLLM-Survey】-【SJTU, AISpeech】-【Type: Survey】`
  - **A Survey on Speech Large Language Models**
  - **Author(s):** Jing Peng, Yucheng Wang, Yu Xi, Xu Li, Xizhuo Zhang, Kai Yu
  - [Paper](https://arxiv.org/pdf/2410.18908v2)

- `【2024-10】-【SpeechLM-Survey】-【CUHK, Tencent】-【Type: Survey】`
  - **Recent Advances in Speech Language Models: A Survey**
  - **Author(s):** Wenqian Cui, Dianzhi Yu, Xiaoqi Jiao, Ziqiao Meng, Guangyan Zhang, Qichao Wang, Yiwen Guo, Irwin King
  - [Paper](https://arxiv.org/pdf/2410.03751)

- `【2024-02】-【AudioLM-Survey】-【National Taiwan University, MIT】-【Type: Survey】`
  - **Towards audio language modeling -- an overview**
  - **Author(s):** Haibin Wu, Xuanjun Chen, Yi-Cheng Lin, Kai-wei Chang, Ho-Lam Chung, Alexander H. Liu, Hung-yi Lee
  - [Paper](https://arxiv.org/abs/2402.13236)

## Multimodal

- `【2024-09】-【EMOVA】-【HKUST】-【Type: Model】`
  - **EMOVA: Empowering Language Models to See, Hear and Speak with Vivid Emotions**
  - **Author(s):** Kai Chen, Yunhao Gou, Runhui Huang, Zhili Liu, Daxin Tan, Jing Xu, Chunwei Wang, Yi Zhu, Yihan Zeng, Kuo Yang, Dingdong Wang, Kun Xiang, Haoyuan Li, Haoli Bai, Jianhua Han, Xiaohui Li, Weike Jin, Nian Xie, Yu Zhang, James T. Kwok, Hengshuang Zhao, Xiaodan Liang, Dit-Yan Yeung, Xiao Chen, Zhenguo Li, Wei Zhang, Qun Liu, Jun Yao, Lanqing Hong, Lu Hou, Hang Xu
  - [Paper](https://arxiv.org/pdf/2409.18042) / [Demo](https://emova-ollm.github.io/)

- `【2023-11】-【CoDi-2】-【UC Berkeley】-【Type: Model】`
  - **CoDi-2: In-Context, Interleaved, and Interactive Any-to-Any Generation**
  - **Author(s):** Zineng Tang, Ziyi Yang, Mahmoud Khademi, Yang Liu, Chenguang Zhu, Mohit Bansal
  - [![GitHub stars](https://img.shields.io/github/stars/main/CoDi-2?style=social)](https://github.com/microsoft/i-Code/tree/main/CoDi-2)
  - [Paper](https://arxiv.org/pdf/2311.18775) / [Demo](https://codi-2.github.io/)

- `【2023-06】-【Macaw-LLM】-【Tencent】-【Type: Model】`
  - **Macaw-LLM: Multi-Modal Language Modeling with Image, Video, Audio, and Text Integration**
  - **Author(s):** Chenyang Lyu, Minghao Wu, Longyue Wang, Xinting Huang, Bingshuai Liu, Zefeng Du, Shuming Shi, Zhaopeng Tu
  - [![GitHub stars](https://img.shields.io/github/stars/lyuchenyang/Macaw-LLM?style=social)](https://github.com/lyuchenyang/Macaw-LLM)
  - [Paper](https://arxiv.org/pdf/2306.09093)

## Study

- `【2024-06】-【Audio Hallucination】-【NTU-Taiwan】-【Type: Research】`
  - **Understanding Sounds, Missing the Questions: The Challenge of Object Hallucination in Large Audio-Language Models**
  - **Author(s):** Chun-Yi Kuan, Wei-Ping Huang, Hung-yi Lee
  - [![GitHub stars](https://img.shields.io/github/stars/kuan2jiu99/audio-hallucination?style=social)](https://github.com/kuan2jiu99/audio-hallucination)
  - [Paper](https://arxiv.org/pdf/2406.08402)

## Safety

- `【2024-06】-【CodecFake】-【National Taiwan University】-【Type: Safety】`
  - **CodecFake: Enhancing Anti-Spoofing Models Against Deepfake Audios from Codec-Based Speech Synthesis Systems**
  - **Author(s):** Haibin Wu, Yuan Tseng, Hung-yi Lee
  - [![GitHub stars](https://img.shields.io/github/stars/roger-tseng/CodecFake?style=social)](https://github.com/roger-tseng/CodecFake)
  - [Paper](https://arxiv.org/abs/2406.07237) / [Other Link](https://codecfake.github.io/)

- `【2024-05】-【VoiceJailbreak】-【CISPA】-【Type: Method】`
  - **Voice Jailbreak Attacks Against GPT-4o**
  - **Author(s):** Xinyue Shen, Yixin Wu, Michael Backes, Yang Zhang
  - [![GitHub stars](https://img.shields.io/github/stars/TrustAIRLab/VoiceJailbreakAttack?style=social)](https://github.com/TrustAIRLab/VoiceJailbreakAttack)
  - [Paper](https://arxiv.org/pdf/2405.19103)

## Chatbot

- `【2025-01】-【MinMo】-【FunAudioLLM Team, Tongyi Lab, Alibaba Group】-【Type: Multimodal Large Language Model】`
  - **MinMo: A Multimodal Large Language Model for Seamless Voice Interaction**
  - **Author(s):** Qian Chen, Yafeng Chen, Yanni Chen, Mengzhe Chen, Yingda Chen, Chong Deng, Zhihao Du, Ruize Gao, Changfeng Gao, Zhifu Gao, Yabin Li, Xiang Lv, Jiaqing Liu, Haoneng Luo, Bin Ma, Chongjia Ni, Xian Shi, Jialong Tang, Hui Wang, Hao Wang, Wen Wang, Yuxuan Wang, Yunlan Xu, Fan Yu, Zhijie Yan, Yexin Yang, Baosong Yang, Xian Yang, Guanrou Yang, Tianyu Zhao, Qinglin Zhang, Shiliang Zhang, Nan Zhao, Pei Zhang, Chong Zhang, Jinren Zhou
  - [Paper](https://arxiv.org/abs/2501.06282) / [Other Link](https://funaudiollm.github.io/minmo)
