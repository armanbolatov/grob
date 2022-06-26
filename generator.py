from transformers import GPT2LMHeadModel, GPT2Tokenizer 

class LyricsGenerator:

    def __init__(self, path: str, use_cuda=False) -> None:
        """
        Инициализирует модель по весам расположенным в
        директории path и заодно гиперпараметры для нее
        """
        self.max_length = 700
        self.repetition_penalty = 1.1
        self.do_sample = True
        self.top_k = 5
        self.top_p = 1
        self.temperature = 1
        self.stop_token = '</s>'
        self.tok = GPT2Tokenizer.from_pretrained(path)
        self.model = GPT2LMHeadModel.from_pretrained(path)
        self.use_cuda = use_cuda
        if self.use_cuda:
            self.model = self.model.cuda()

    def update_params(self, **kwargs) -> None:
        """
        Обновляет параметры нашей модели и выдает ошибку
        если соответствующего параметра нет
        """
        for key, value in kwargs.items():
            params = set(self.__dict__.keys()) - \
                     set(["model", "use_gpu", "tok"])
            if key not in params:
                raise Exception(f"Invalid key: {key}")
            self.__dict__[key] = value


    def generate(self, song_name: str) -> str:
        """
        Возвращает стринг, который содержит текст песни
        сгенерированный по заданному названию song_name
        """
        # токенизириуем входной текст
        text = f"<s>Название песни: {song_name}\nТекст песни:"
        input = self.tok.encode(text, return_tensors="pt")

        # собираем словарь с параметрами для gpt2 модели
        # это все поля класса кроме model и token
        params = {x: self.__dict__[x] \
            for x in self.__dict__ if x not in ["model", "tok"]}

        # даем входной ембеддинг и параметры для нашей модельки
        if self.use_cuda:
            input = input.cuda()
        out = self.model.generate(input, **params)
        output_text = self.tok.decode(out[0])

        try:
            # оказывается, что модель выдает песню не только по
            # заданному названию, но и по другим рандомным названиям.
            # поэтому урезаем все что идет после стоп-токена </s>
            res = str(output_text[:output_text.index("</s>") + 1])[:-1]
        except:
            # если стоп токена </s> нет, значит текст содержит более
            # max_tokens токенов в таком случае оставляем все как есть
            res = output_text
        # убираем первые две строчки содержащие "Текст песни:" и название
        res = res.split("\n", 2)[2]
        return res