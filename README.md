## Getting Started

### Installation

- make sure you have `python3` or above and `pip` installed on your machine

#### Clone the Repository
```bash
git clone https://github.com/tedxsvv/tedsvv2022.git
cd ./tedsvv2022

pip install virtualenv
```

#### Vitual Environment

```bash
virtualenv ./virt             # unix
python3 -m venv ./virt        #if above command fails, run this command

virtualenv %HOMEPATH%\virt    # windows

source ./virt/bin/activate          # unix
%HOMEPATH%\virt\Scripts\activate    # windows
```

#### Dependencies

```bash
pip install -r requirements.txt
```
#### Run server
```bash
py manage.py runserver          # windows
python3 manage.py runserver     # unix
```
