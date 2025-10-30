# dss-quiz5 – Perceptron Devam Çalışması

Bu proje, verilen ağırlıklardan (iteration4 sonrası) başlayarak perceptron eğitimini iteration5'ten itibaren sürdürür. Dört ardışık E=0 elde edilene kadar (beklenen: iteration11–14) her adımı ve olası ağırlık güncellemelerini yazdırır. Sonunda X1=X2=X3=0.5 için tahmini döndürür.

## Çalıştırma
PowerShell tarzı ayraçla tek satırda çalıştırmak isterseniz:

```powershell
python .\perceptron_continue.py; echo "Done"
```

Veya tek komut:

```powershell
python .\perceptron_continue.py
```

## Beklenen Özet
- Dört ardışık sıfır hata: iteration11–iteration14
- Nihai ağırlıklar: W1=0.8, W2=-0.2, W3=-0.1
- X1=X2=X3=0.5 için: Net=0.25, Theta=0.5 => Y=0

