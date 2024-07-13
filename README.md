## Scheduling System

### Description
A system designed to manage and schedule appointments efficiently, ensuring that sellers are not double-booked.

### Objective
To provide a scheduling solution that includes appointment creation, conflict validation, and a calendar view.

## Installation Instructions

### Prerequisites
- Python 3.x
- Frappe Framework
- MySQL

### Installation Steps

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the bench directory:
    ```bash
    cd $PATH_TO_YOUR_BENCH
    ```

3. Get the app:
    ```bash
    bench get-app <URL_OF_THIS_REPO> --branch develop
    ```

4. Install the app:
    ```bash
    bench install-app scheduling_system
    ```

## Configuration Details

### Activate Developer Mode
To edit/create DocTypes, activate developer mode:
```bash
bench set-config developer_mode 1
```
## Configuration Files

- `site_config.json`: Adjust settings as needed.

## Database Schema

### DocTypes

#### Appointment DocType:
- **Client Name**: Data
- **Start date**: Datetime
- **End date**: Datetime (Read-only, set programmatically based on the start date and duration)
- **Duration**: Time
- **Description**: Small Text
- **Seller**: Link (Links to a User)
- **Status**: Select (Options: Scheduled, Finished, Canceled)

## Key Features

- **Appointment Creation**: Users can create appointments with specified details.
- **Conflict Validation**: Ensures that a seller cannot have overlapping appointments.
- **Calendar View**: Configured as the default view for appointments.

## Usage Instructions

### Creating an Appointment
1. Log in to the system.
2. Navigate to the Appointments module.
3. Click on "New Appointment."
4. Fill in the required fields and save.

### Calendar View
1. Navigate to the Appointments module.
2. The calendar view is set as the default view, displaying all appointments.

## Code Documentation

### Code Structure
- `apps/scheduling_system`: Main app directory.
- `doctype/appointment`: Contains the Appointment DocType.
  - `appointment.py`: Backend logic for Appointment Doctype.
  - `appointment.js`: Client-side logic for Appointment Doctype.
  - `appointment_calendar.js`: JavaScript for calendar view.

### Key Modules

#### appointment.py
Handles backend logic for appointment management.

#### appointment.js
Handles client-side interactions for creating and managing appointments.

#### appointment_calendar.js
Configures and manages the calendar view for appointments.

## API Documentation

### Endpoints

#### Retrieve Appointments
- **Method**: GET
- **Endpoint**: `/api/appointments`
- **Response**:
    ```json
    [
      {
        "client_name": "John Doe",
        "start_date": "2024-07-15T10:00:00",
        "end_date": "2024-07-15T11:00:00",
        "seller": "seller_1",
        "status": "Scheduled"
      }
    ]
    ```

#### Create Appointment
- **Method**: POST
- **Endpoint**: `/api/appointments`
- **Request**:
    ```json
    {
      "client_name": "John Doe",
      "start_date": "2024-07-15T10:00:00",
      "end_date": "2024-07-15T11:00:00",
      "seller": "seller_1",
      "status": "Scheduled"
    }
    ```
- **Response**:
    ```json
    {
      "message": "Appointment created successfully"
    }
    ```

## Considerações Finais

### Possíveis Melhorias no Sistema
- **Integração com APIs Externas**: Adicionar integração com serviços de calendário como Google Calendar e Outlook para sincronização de compromissos.
- **Notificações e Lembretes**: Implementar sistema de notificações e lembretes para alertar clientes e vendedores sobre compromissos agendados.
- **Relatórios e Análises**: Desenvolver módulos para geração de relatórios e análise de dados, permitindo aos usuários obter insights sobre a utilização e desempenho do sistema.
- **Aprimoramento da Interface de Usuário**: Melhorar a interface de usuário para torná-la mais intuitiva e acessível.
- **Suporte a Múltiplos Idiomas**: Adicionar suporte a múltiplos idiomas para atender a um público mais amplo.

### Dificuldades Encontradas no Projeto
- **Gerenciamento de Conflitos de Horário**: Implementar a validação para evitar conflitos de agendamento foi um desafio significativo, exigindo lógica complexa para garantir que um vendedor não seja agendado para múltiplos compromissos simultâneos.
- **Configuração do Ambiente de Desenvolvimento**: Configurar corretamente o ambiente de desenvolvimento com todas as dependências necessárias foi uma tarefa demorada.
- **Integração com Framework Frappe**: Adaptar o projeto para funcionar de forma otimizada dentro do framework Frappe exigiu um entendimento profundo de sua arquitetura e melhores práticas.
- **Manutenção da Qualidade do Código**: Garantir que o código fosse bem estruturado e atendesse aos padrões de qualidade, utilizando ferramentas de linting e formatação, apresentou desafios durante o desenvolvimento colaborativo.


## Pre-commit Configuration

Pre-commit is configured to use the following tools for checking and formatting your code:
- ruff
- eslint
- prettier
- pyupgrade

## License
This project is licensed under the MIT License.

Feel free to paste this markdown text into your GitHub repository's README file.
