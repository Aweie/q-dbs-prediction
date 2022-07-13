{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "534bc6de",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template,request"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ff1fb1db",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "80188bd5",
   "metadata": {},
   "outputs": [],
   "source": [
    "app=Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a93b6a66",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route (\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method==\"POST\":\n",
    "        rates=float(request.form.get(\"rates\"))\n",
    "        print(rates)\n",
    "        model=joblib.load(\"regression\")\n",
    "        pred=model.predict([[rates]])\n",
    "        return (render_template(\"index.html\",result=pred))\n",
    "    else:\n",
    "        return (render_template(\"index.html\",result=\"WAITING\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58b76eb5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [07/Jul/2022 17:13:22] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [07/Jul/2022 17:13:28] \"POST / HTTP/1.1\" 200 -\n",
      "[2022-07-07 17:13:29,214] ERROR in app: Exception on / [POST]\n",
      "Traceback (most recent call last):\n",
      "  File \"D:\\anaconda3\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"D:\\anaconda3\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"D:\\anaconda3\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"D:\\anaconda3\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"D:\\anaconda3\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"D:\\anaconda3\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"C:\\Users\\86156\\AppData\\Local\\Temp/ipykernel_13160/3538767505.py\", line 4, in index\n",
      "    rates=float(request.form.get(\"rates\"))\n",
      "ValueError: could not convert string to float: ''\n",
      "127.0.0.1 - - [07/Jul/2022 17:13:29] \"POST / HTTP/1.1\" 500 -\n",
      "127.0.0.1 - - [07/Jul/2022 17:15:59] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [07/Jul/2022 17:16:08] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4\n"
     ]
    }
   ],
   "source": [
    "if __name__ ==\"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0848a4dd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0dd2d918",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
