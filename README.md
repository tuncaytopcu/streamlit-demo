# Ka|Ve Streamlit Demo


# Açıklama

Bu çalışma kapsamında temel bir streamlit uygulaması geliştireceğiz. Bu uygulama ile verilen metnin duygusunu [sumapi](https://pypi.org/project/sumapi/) kütüphanesi ile tespit edeceğiz. Ardından metnin duygusunu streamlit uygulamasının komponentlerinden yararlanarak ekrana yazdıracağız. 

# Yerel Makine'de Kurulum ve Çalıştırma

Uygulamanın hatasız çalışabilmesi requirements.txt içerisinde bulunan kütüphanelerin yüklenmesi gerekmektedir. Bunu yapmak için alttaki kodu kullanabilirsiniz.

```
pip install -r requirements.txt
```

Bu kod ile gerekli kütüphaneleri kurduktan sonra uygulamayı başlatmak için alttaki komutu kullanabilirsiniz. 

Not: Öncelikle kod ile aynı dizine gitmeniz gerekmektedir.

```
streamlit run app.py --server.port 8080
```

Bu kodu çalıştırdıktan sonra http://localhost:8080 portunda uygulamanın çalıştığını gözlemleyeceksiniz. 


# AWS üzerinde Canlıya Alma

- AWS üzerinde uygulamanın canlıya alınabilmesi için öncelikle [AWS EC2](https://us-east-1.console.aws.amazon.com/ec2/) servisi üzerinden 1GB RAM 1VCPU'ya sahip bir makine açılması gerekmektedir. Makine tipi olarak ücretsiz olduğu için t2.micro tercih edilebilir. 
- Ayarlar yapılırken security group ayarında bütün portlar(önerilmez veya streamlit uygulamasının yayınlanacağı porta erişim verilmesi gerekmektedir. 
- Makine açıldıktan sonra makineye ssh veya ec2-serial-console kullanılarak erişilebilir.
- Amazon makineleri yüksek ihtimalle python3 yüklü olarak gelmektedir. Eğer gelmediyse internet üzerinden Debian/Linux makinelere nasıl python yükleneceğine bakabilirsiniz.
- Makineye gerekli kodların çekilebilmesi için git yüklenir. 
```
# AWS AMI
yum install git -y

# Farklı Makineler
apt-get install git -y
```

- Git yüklendikten sonra alttaki komut ile kodlar makineye çekilir.
```
git clone https://github.com/kaveai/streamlit-demo.git
```

ardından alttaki komut ile dosyalara girilir.

```
cd streamlit-demo/
```

Gerekli kütüphaneler yüklenir. 

Not: Makinede pip bulunmuyorsa ```yum install python3-pip -y```komuduyla kurulabilir.

```
pip install -r requirements.txt
```

Uygulama çalıştırılır. 

Not: Uygulama çalıştırılırken dış ağa açılabilmesi için alttaki komutun çalıştırılması gerekmektedir. 

```
streamlit run app.py --server.port 8080 --server.address 0.0.0.0
```

Uygulama çalışınca alttaki gibi bir çıktı gelecektir. Bu çıktıda alttaki ip adresine girilerek uygulamaya erişilebilir. 

```
Çıktı Eklenecek.
```
