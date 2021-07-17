Title: 如何利用Flask WTForm快速建立表單
Description: 利用Python code快數建立出Web Form讓使用者可以填寫並上傳資料。
Authors: GGFU
Date:17/07/2021
Tags: 
ID: flask_wtform
base_url: https://ggfu0114.github.io/

# Flask WTForm

> Server Flask Side

在 Flask App 的程式碼裡面，我們可以利用python的程式碼去定義From的內容物，並呈現在網頁上給使用者填入資料跟上傳。

首現要先創立出繼承`FlaskForm`的 class，並在class裡面去定義裡面有什麼欄位。在預設的情況下，這些欄位會被依序的放置在網頁上。欄位有分很多種不同的型態(例如：輸入欄位，下拉選單，日期選擇器...)。在[官網](https://wtforms.readthedocs.io/en/2.3.x/fields/)可以查到這個套件所提供的不同型態。

```py
class MyForm(FlaskForm):
    name = StringField('Name')
    email = EmailField('Email')
    
```

完成定義表單的形式後，並須將整個Form物件初始化，如此一來可以將整個form物件傳給Template去呈現出來。

```py
form = MyForm()
return render_template('index.html', form=form)
```

> Template Side

在Jinja Template這一側，我們不需要去寫Form html的程式碼，因為Flask WTForm有預先幫我們定義了這各個元素的html程式碼

```html
<p>{{ form.name.label }} {{ form.name(size=20) }}</p>
<p>{{ form.email.label }} {{ form.email }}</p>
```

form這個變數裡面，包含所有的欄位，我們可以自己編排這些欄位的顯示順序。

## Flask form

Create a form for user to fill in the data and post to the server. The upload photo will be saved in the photo folder
with `.jpg` as the extension. More field type example, please refer to the
official [website](https://wtforms.readthedocs.io/en/2.3.x/fields/).
