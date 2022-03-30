from django.db import models


class IndexMenu(models.Model):
    CHOICES = (
        (1, '#stages'),
        (2, '#cases'),
        (3, '#reviews'),
        (4, '#faq'),
        (5, '#request')
    )
    menu = models.CharField(verbose_name='Название для пользователя', max_length=300, help_text="Как мы работаем?")
    menu_context = models.IntegerField(verbose_name='Название блока', choices=CHOICES)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return 'Меню:  ' + self.menu + ' ведет на блок: ' + self.get_menu_context_display()


class IndexPhone(models.Model):
    PhoneOne = models.CharField(verbose_name='Код оператора', max_length=300, help_text="+ 7 (967)")
    PhoneTwo = models.CharField(verbose_name='Номер телефона', max_length=300, help_text="555 - 49 - 52")

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номер телефона'

    def __str__(self):
        return 'Актуальный номер: ' + self.PhoneOne + ' ' + self.PhoneTwo


class IndexHowToWork(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to='media/')
    rows = models.IntegerField(verbose_name='Какой шаг?', help_text='1, 2, 3, 4')
    title = models.CharField(verbose_name='Наименование шага', max_length=300)
    content = models.TextField(verbose_name='Описание шага')

    class Meta:
        verbose_name = 'Этапы создания проекта'
        verbose_name_plural = 'Этапы создания проекта'

    def __str__(self):
        return 'Наименование этапа: {} Номер этапа: {}'.format(self.title, self.rows)


class IndexCases(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to='media/')
    Hash = models.CharField(verbose_name='#ХешТеги', max_length=1000)
    title = models.CharField(verbose_name='Заголовок кейса', max_length=500)
    content_left = models.TextField(verbose_name='Особенности')
    content_center = models.TextField(verbose_name='Задачи')
    content_footer = models.TextField(verbose_name='Решения')
    content_footer2 = models.TextField(verbose_name='Результат')

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'

    def __str__(self):
        return 'Наименование кейса: {}'.format(self.title)


class IndexReview(models.Model):
    """ Отзывы """
    image = models.ImageField(verbose_name='Изображение', upload_to='media/')
    content = models.TextField(verbose_name='Содержание отзыва')
    name = models.CharField(verbose_name='ФИО', max_length=300)
    city = models.CharField(verbose_name='Город', max_length=300)

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return 'Отзыв: от пользователя {} из города {}'.format(self.name, self.city)


class IndexFAQ(models.Model):
    """ ЧАВО """
    title = models.CharField(verbose_name='Название', max_length=300)
    content = models.TextField(verbose_name='Содержание')

    class Meta:
        verbose_name = 'Ответы на частые вопросы'
        verbose_name_plural = 'Ответы на частые вопросы'

    def __str__(self):
        return 'Ответ на вопрос: {}'.format(self.title)


class Police(models.Model):
    file = models.FileField(verbose_name='Политика конфиденциальности', upload_to='media/')

    class Meta:
        verbose_name = 'Политика конфиденциальности'
        verbose_name_plural = 'Политика конфиденциальности'

    def __str__(self):
        return 'Политика конфиденциальности'


class UserAccept(models.Model):
    file = models.FileField(verbose_name='Пользовательское соглашение', upload_to='media/')

    class Meta:
        verbose_name = 'Пользовательское соглашение'
        verbose_name_plural = 'Пользовательское соглашение'

    def __str__(self):
        return 'Пользовательское соглашение'


class ArticleImage(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    many_image = models.ForeignKey(IndexCases, on_delete=models.CASCADE)


class ModelBackForm(models.Model):
    minPrice = models.CharField(verbose_name='Минимальная сумма', max_length=300)
    maxPrice = models.CharField(verbose_name='Максимальная сумма', max_length=300)
    service = models.CharField(verbose_name='Услуга', max_length=300)
    name = models.CharField(verbose_name='Имя клиента', max_length=300)
    email = models.CharField(verbose_name='Почта клиента', max_length=300)
    phone = models.CharField(verbose_name='Телефон клиента', max_length=300)
    file = models.FileField(verbose_name='Файл проекта', upload_to='media/')
    message = models.TextField(verbose_name='Сообщение от клиента')

    class Meta:
        verbose_name = 'Форму обратной связи'
        verbose_name_plural = 'Форма обратной связи'

    def __str__(self):
        return 'Заказ от клиента: ' + self.name + ' На тему: ' + self.service
