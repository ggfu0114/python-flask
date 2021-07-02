# First Flask

## 檔案介紹
`main.py`: 整個Flask APP 主要的進入檔案
`requirement.txt`: 執行APP所需要的相依套件(開發工程師不可能所有功能都自己獨立製作，所以需要很多Open Source的套件來輔助，完成一套用的系統)

## 程式碼解說
```py
@app.route('/')
```
URL的入口點，當使用者打錯網址時， APP沒有辦法找到對應的function來處理時，就會出現 *404 not found* 的錯誤。

```py
return "<div>Hello World, gFu.<div>"
```
當使用者連上正確的URL時，APP就會幫忙處理資料，但是這個簡單的範例並沒多加複雜的邏輯，只有回傳單純的html元素給使用者。
