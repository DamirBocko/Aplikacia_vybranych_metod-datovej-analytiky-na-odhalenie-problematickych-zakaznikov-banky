# Inštalácia knižníc a modulov
import numpy as np # Importuje knižnicu NumPy pre vedecké výpočty
import pandas as pd # Importuje knižnicu pandas pre manipuláciu s dátami
import seaborn as sns
#from ydata_profiling import ProfileReport # Importuje triedu ProfileReport z knižnice ydata_profiling pre tvorbu profilov dát
import tabulate #  Importuje knižnicu tabulate pre formátovanie tabuliek
import matplotlib.pyplot as plt # Importuje modul pyplot z knižnice matplotlib pre tvorbu grafov
from sklearn.cluster import KMeans # Importuje triedu KMeans z modulu cluster z knižnice scikit-learn pre zhlukovanie
from sklearn.model_selection import GridSearchCV # Importuje triedu GridSearchCV z modulu model_selection z knižnice scikit-learn pre vyhľadávanie optimálnych parametrov
from sklearn.preprocessing import LabelEncoder # Importuje triedu LabelEncoder z modulu preprocessing z knižnice scikit-learn pre zakódovanie kategorických premenných
from sklearn.ensemble import RandomForestClassifier #  Importuje triedu RandomForestClassifier z modulu ensemble z knižnice scikit-learn pre klasifikáciu pomocou random forest
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split