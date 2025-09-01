# English

# Coffee Shop API ☕  
This is a simple API for a Coffee Shop built with **Python** and **FastAPI**.  
The project demonstrates a **Modular Monolith** architecture, where each module follows a **Layered / Clean Architecture** approach.  

## Technologies 🛠️  
* **Backend**: Python 3.11+, FastAPI  
* **Database**: MySQL  
* **ORM**: SQLAlchemy 2.0  
* **Data Validation**: Pydantic V2  
* **Web Server**: Uvicorn  

## Architecture 🏛️  

The project is built on two main architectural principles that ensure code organization, maintainability, and scalability.  

### 1. High Level — Modular Monolith  

The application is a single deployable unit (monolith), which makes it simple to run and deploy.  
However, internally it is logically divided into independent **modules** (e.g., `products`, `orders`).  
Each module is responsible for one specific business domain.  

**Advantages:**  
* **Organized code:** Easy to locate files related to a specific domain.  
* **Low coupling:** Modules are as independent from each other as possible.  
* **Easy scalability:** Adding new functionality simply means creating a new module.  

### 2. Module Level — Layered Architecture  

Each module is divided into 4 main layers, where every layer has its own responsibility:  

```
┌──────────────────┐      ┌──────────────────┐      ┌────────────────────┐      ┌──────────┐
│ Presentation     │──────▶│ Application      │──────▶│ Infrastructure     │──────▶│ Database │
│ (router.py)      │      │ (services.py)    │      │ (repositories.py)  │      │ (MySQL)  │
└──────────────────┘      └──────────────────┘      └────────────────────┘      └──────────┘
         ▲                      ▲                             ▲
         │                      │                             │
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│ Domain (Schemas) │◀─────┤ Domain (Schemas) │      │ Domain (Models)  │
└──────────────────┘      └──────────────────┘      └──────────────────┘
```


1. **Presentation Layer**  
   * **File:** `router.py`  
   * **Role:** Defines API endpoints, handles HTTP requests, and formats responses.  
     This is the only layer that communicates with the outside world.  

2. **Application Layer**  
   * **File:** `services.py`  
   * **Role:** Implements the core business logic of the application.  
     It coordinates operations by calling repositories.  
     This is the "brain" of the module.  

3. **Domain Layer**  
   * **Files:** `models.py`, `schemas.py`  
   * **Role:** Defines data structures.  
     * `models.py`: SQLAlchemy models describing database tables.  
     * `schemas.py`: Pydantic schemas acting as the "data interface" for the API (validation & serialization).  

4. **Infrastructure Layer**  
   * **File:** `repositories.py`  
   * **Role:** Handles direct interaction with the database.  
     This layer isolates all persistence logic from the rest of the application.  

## Project Structure 📂  

```sh
coffee_shop/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application setup
│   ├── core/
│   │   ├── database.py         # SQLAlchemy configuration
│   │   └── ...
│   └── modules/
│       ├── products/           # "Products" module
│       │   ├── presentation/
│       │   │   └── router.py
│       │   ├── application/
│       │   │   └── services.py
│       │   ├── domain/
│       │   │   ├── models.py
│       │   │   └── schemas.py
│       │   └── infrastructure/
│       │       └── repositories.py
│       └── orders/             # "Orders" module (future)
├── .env.example                # Example .env file
├── requirements.txt            # Dependencies
└── ...
```

- - -
# Armenian

# Coffee Shop API ☕

Սա Coffee Shop-ի համար նախատեսված պարզ API է՝ կառուցված Python-ի և FastAPI-ի միջոցով։ Նախագիծը ցուցադրում է **Մոդուլային Մոնոլիտ (Modular Monolith)** ճարտարապետություն, որտեղ յուրաքանչյուր մոդուլ իր հերթին հետևում է **Շերտավորված (Layered / Clean Architecture)** մոտեցմանը։

## Տեխնոլոգիաներ 🛠️

* **Backend**: Python 3.11+, FastAPI
* **Տվյալների բազա**: MySQL
* **ORM**: SQLAlchemy 2.0
* **Տվյալների վալիդացում**: Pydantic V2
* **Web Server**: Uvicorn

## Ճարտարապետություն (Architecture) 🏛️

Նախագիծը կառուցված է երկու հիմնական ճարտարապետական սկզբունքների վրա, որոնք ապահովում են կոդի կազմակերպվածություն, սպասարկման հեշտություն և մասշտաբայնություն։

### 1. Բարձր մակարդակ՝ Մոդուլային Մոնոլիտ

Հավելվածը մեկ ամբողջական միավոր է (մոնոլիտ), որը հեշտ է գործարկել և տեղակայել։ Սակայն ներսից այն տրամաբանորեն բաժանված է անկախ **մոդուլների** (օրինակ՝ `products`, `orders`)։ Յուրաքանչյուր մոդուլ պատասխանատու է բիզնեսի մեկ կոնկրետ տիրույթի համար։

**Առավելությունները:**
* **Կազմակերպված կոդ:** Հեշտ է գտնել կոնկրետ տիրույթին վերաբերող ֆայլերը։
* **Ցածր կապակցվածություն (Low Coupling):** Մոդուլները հնարավորինս անկախ են միմյանցից։
* **Հեշտ մասշտաբայնություն:** Նոր ֆունկցիոնալ ավելացնելու համար պարզապես ստեղծվում է նոր մոդուլ։

### 2. Մոդուլի մակարդակ՝ Շերտավորված ճարտարապետություն

Յուրաքանչյուր մոդուլ իր ներսում բաժանված է 4 հիմնական շերտի, որտեղ յուրաքանչյուրն ունի իր հստակ պատասխանատվությունը։

```
┌──────────────────┐      ┌──────────────────┐      ┌────────────────────┐      ┌──────────┐
│ Presentation     │──────▶│ Application      │──────▶│ Infrastructure     │──────▶│ Database │
│ (router.py)      │      │ (services.py)    │      │ (repositories.py)  │      │ (MySQL)  │
└──────────────────┘      └──────────────────┘      └────────────────────┘      └──────────┘
         ▲                      ▲                             ▲
         │                      │                             │
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│ Domain (Schemas) │◀─────┤ Domain (Schemas) │      │ Domain (Models)  │
└──────────────────┘      └──────────────────┘      └──────────────────┘
```

1.  **Presentation Layer (Ներկայացման շերտ):**
    * **Ֆայլ:** `router.py`
    * **Դերը:** API endpoint-ների սահմանում, HTTP հարցումների ընդունում և պատասխանների ձևավորում։ Սա միակ շերտն է, որը «շփվում» է արտաքին աշխարհի հետ։

2.  **Application Layer (Բիզնես տրամաբանության շերտ):**
    * **Ֆայլ:** `services.py`
    * **Դերը:** Հավելվածի հիմնական բիզնես տրամաբանության իրականացում։ Այն համակարգում է գործողությունները՝ կանչելով repository-ներին։ Սա մոդուլի «ուղեղն» է։

3.  **Domain Layer (Դոմեյնի շերտ):**
    * **Ֆայլեր:** `models.py`, `schemas.py`
    * **Դերը:** Տվյալների կառուցվածքների սահմանում։
        * `models.py`: SQLAlchemy մոդելներ, որոնք նկարագրում են տվյալների բազայի աղյուսակները։
        * `schemas.py`: Pydantic սխեմաներ, որոնք հանդես են գալիս որպես «տվյալների ինտերֆեյս» API-ի համար (վալիդացիա և սերիալիզացիա)։

4.  **Infrastructure Layer (Ենթակառուցվածքի շերտ):**
    * **Ֆայլ:** `repositories.py`
    * **Դերը:** Տվյալների բազայի հետ ուղիղ աշխատանք։ Այս շերտը մեկուսացնում է տվյալների հետ աշխատանքի ամբողջ տրամաբանությունը հավելվածի մնացած մասից։

## Նախագծի Կառուցվածքը 📂

```sh
coffee_shop/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI հավելվածի ստեղծում
│   ├── core/
│   │   ├── database.py         # SQLAlchemy-ի կոնֆիգուրացիա
│   │   └── ...
│   └── modules/
│       ├── products/           # «Ապրանքներ» մոդուլ
│       │   ├── presentation/
│       │   │   └── router.py
│       │   ├── application/
│       │   │   └── services.py
│       │   ├── domain/
│       │   │   ├── models.py
│       │   │   └── schemas.py
│       │   └── infrastructure/
│       │       └── repositories.py
│       └── orders/             # «Պատվերներ» մոդուլ (ապագայում)
│
├── .env.example                # .env ֆայլի օրինակ
├── requirements.txt            # Պահանջվող գրադարաններ
└── ...
```

## Տեղադրում և Կարգավորում ⚙️

1.  **Clone արեք repository-ն:**
    ```bash
    git clone <your-repository-url>
    cd <repository-folder>
    ```

2.  **Ստեղծեք և ակտիվացրեք վիրտուալ միջավայր (virtual environment):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Տեղադրեք անհրաժեշտ գրադարանները:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Կարգավորեք տվյալների բազան:**
    * Պատճենեք `.env.example` ֆայլը և անվանափոխեք այն `.env`։
    * `.env` ֆայլի մեջ լրացրեք ձեր MySQL տվյալների բազայի միացման տվյալները։
    ```
    DATABASE_URL="mysql+mysqlclient://USER:PASSWORD@HOST/DB_NAME"
    ```

## Ինչպես աշխատեցնել 🚀

Նախագծի հիմնական թղթապանակից գործարկեք հետևյալ հրամանը.

```bash
uvicorn app.main:app --reload
```

Հավելվածը հասանելի կլինի `http://127.0.0.1:8000` հասցեով։

API-ի ավտոմատ сгенерированный փաստաթղթավորումը (Swagger UI) կարող եք գտնել այստեղ՝ `http://127.0.0.1:8000/docs`։
