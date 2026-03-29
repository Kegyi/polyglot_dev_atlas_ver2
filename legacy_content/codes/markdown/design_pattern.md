# Codes registry — design_pattern

This file contains code snippets exported from legacy_content/codes_registry.json.
Edit this file and run `scripts/update_registry_from_md.py` to push changes back.

## abstract_factory

- Docs: /legacy_content/docs/design_pattern/abstract_factory/README.md

<!-- REGISTRY_PATH: abstract_factory.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>
#include <string>

struct Button {
    virtual ~Button() = default;
    virtual std::string render() const = 0;
};

struct Dialog {
    virtual ~Dialog() = default;
    virtual std::string render() const = 0;
};

struct WidgetFactory {
    virtual ~WidgetFactory() = default;
    virtual std::unique_ptr<Button> createButton() const = 0;
    virtual std::unique_ptr<Dialog> createDialog() const = 0;
};

struct LightButton : Button {
    std::string render() const override { return "light button"; }
};

struct LightDialog : Dialog {
    std::string render() const override { return "light dialog"; }
};

struct DarkButton : Button {
    std::string render() const override { return "dark button"; }
};

struct DarkDialog : Dialog {
    std::string render() const override { return "dark dialog"; }
};

struct LightFactory : WidgetFactory {
    std::unique_ptr<Button> createButton() const override { return std::make_unique<LightButton>(); }
    std::unique_ptr<Dialog> createDialog() const override { return std::make_unique<LightDialog>(); }
};

struct DarkFactory : WidgetFactory {
    std::unique_ptr<Button> createButton() const override { return std::make_unique<DarkButton>(); }
    std::unique_ptr<Dialog> createDialog() const override { return std::make_unique<DarkDialog>(); }
};

void showScreen(const WidgetFactory& factory) {
    auto button = factory.createButton();
    auto dialog = factory.createDialog();
    std::cout << button->render() << " + " << dialog->render() << '\n';
}

int main() {
    LightFactory light;
    DarkFactory dark;
    showScreen(light);
    showScreen(dark);
}
// __ROUNDTRIP_TEST__
```

<!-- REGISTRY_PATH: abstract_factory.languages.go -->
### go

```go
package main

import "fmt"

type Button interface{ Render() string }
type Dialog interface{ Render() string }

type WidgetFactory interface {
	CreateButton() Button
	CreateDialog() Dialog
}

type LightButton struct{}

func (LightButton) Render() string { return "light button" }

type LightDialog struct{}

func (LightDialog) Render() string { return "light dialog" }

type DarkButton struct{}

func (DarkButton) Render() string { return "dark button" }

type DarkDialog struct{}

func (DarkDialog) Render() string { return "dark dialog" }

type LightFactory struct{}

func (LightFactory) CreateButton() Button { return LightButton{} }
func (LightFactory) CreateDialog() Dialog { return LightDialog{} }

type DarkFactory struct{}

func (DarkFactory) CreateButton() Button { return DarkButton{} }
func (DarkFactory) CreateDialog() Dialog { return DarkDialog{} }

func showScreen(factory WidgetFactory) {
	button := factory.CreateButton()
	dialog := factory.CreateDialog()
	fmt.Printf("%s + %s\n", button.Render(), dialog.Render())
}

func main() {
	showScreen(LightFactory{})
	showScreen(DarkFactory{})
}
```

<!-- REGISTRY_PATH: abstract_factory.languages.python -->
### python

```python
from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...


class Dialog(ABC):
    @abstractmethod
    def render(self) -> str: ...


class WidgetFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...

    @abstractmethod
    def create_dialog(self) -> Dialog: ...


class LightButton(Button):
    def render(self) -> str:
        return "light button"


class LightDialog(Dialog):
    def render(self) -> str:
        return "light dialog"


class DarkButton(Button):
    def render(self) -> str:
        return "dark button"


class DarkDialog(Dialog):
    def render(self) -> str:
        return "dark dialog"


class LightFactory(WidgetFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_dialog(self) -> Dialog:
        return LightDialog()


class DarkFactory(WidgetFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_dialog(self) -> Dialog:
        return DarkDialog()


def show_screen(factory: WidgetFactory) -> None:
    print(f"{factory.create_button().render()} + {factory.create_dialog().render()}")


show_screen(LightFactory())
show_screen(DarkFactory())
```

<!-- REGISTRY_PATH: abstract_factory.languages.scala -->
### scala

```scala
// Abstract Factory
trait UIElement

case class Button(label: String) extends UIElement
case class Checkbox(label: String) extends UIElement

trait UIFactory {
  def createButton(label: String): Button
  def createCheckbox(label: String): Checkbox
}

object LightThemeFactory extends UIFactory {
  def createButton(label: String): Button = Button(s"Light Button: $label")
  def createCheckbox(label: String): Checkbox = Checkbox(s"Light Checkbox: $label")
}

object DarkThemeFactory extends UIFactory {
  def createButton(label: String): Button = Button(s"Dark Button: $label")
  def createCheckbox(label: String): Checkbox = Checkbox(s"Dark Checkbox: $label")
}

object Main extends App {
  val lightFactory: UIFactory = LightThemeFactory
  val darkFactory: UIFactory = DarkThemeFactory
  
  println(lightFactory.createButton("OK"))
  println(darkFactory.createButton("OK"))
}
```

<!-- REGISTRY_PATH: abstract_factory.languages.typescript -->
### typescript

```typescript
interface Button {
  render(): string;
}

interface Dialog {
  render(): string;
}

interface WidgetFactory {
  createButton(): Button;
  createDialog(): Dialog;
}

class LightButton implements Button {
  render(): string {
    return 'light button';
  }
}

class LightDialog implements Dialog {
  render(): string {
    return 'light dialog';
  }
}

class DarkButton implements Button {
  render(): string {
    return 'dark button';
  }
}

class DarkDialog implements Dialog {
  render(): string {
    return 'dark dialog';
  }
}

class LightFactory implements WidgetFactory {
  createButton(): Button {
    return new LightButton();
  }

  createDialog(): Dialog {
    return new LightDialog();
  }
}

class DarkFactory implements WidgetFactory {
  createButton(): Button {
    return new DarkButton();
  }

  createDialog(): Dialog {
    return new DarkDialog();
  }
}

function showScreen(factory: WidgetFactory): void {
  console.log(`${factory.createButton().render()} + ${factory.createDialog().render()}`);
}

showScreen(new LightFactory());
showScreen(new DarkFactory());
```

## adapter

- Docs: /legacy_content/docs/design_pattern/adapter/README.md

<!-- REGISTRY_PATH: adapter.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>

struct Printer {
    virtual ~Printer() = default;
    virtual void print(const std::string& message) const = 0;
};

class JsonLogger {
public:
    void writeJson(const std::string& payload) const {
        std::cout << payload << '\n';
    }
};

class JsonLoggerAdapter : public Printer {
public:
    explicit JsonLoggerAdapter(const JsonLogger& logger) : logger_(logger) {}

    void print(const std::string& message) const override {
        logger_.writeJson("{\"message\":\"" + message + "\"}");
    }

private:
    const JsonLogger& logger_;
};

int main() {
    JsonLogger logger;
    JsonLoggerAdapter printer(logger);
    printer.print("build finished");
}
```

<!-- REGISTRY_PATH: adapter.languages.go -->
### go

```go
package main

import "fmt"

type Printer interface {
	Print(message string)
}

type JSONLogger struct{}

func (JSONLogger) WriteJSON(payload string) {
	fmt.Println(payload)
}

type JSONLoggerAdapter struct {
	logger JSONLogger
}

func (a JSONLoggerAdapter) Print(message string) {
	a.logger.WriteJSON(fmt.Sprintf("{\"message\":\"%s\"}", message))
}

func main() {
	printer := JSONLoggerAdapter{logger: JSONLogger{}}
	printer.Print("build finished")
}
```

<!-- REGISTRY_PATH: adapter.languages.python -->
### python

```python
from dataclasses import dataclass


class Printer:
    def print(self, message: str) -> None:
        raise NotImplementedError


class JsonLogger:
    def write_json(self, payload: str) -> None:
        print(payload)


@dataclass
class JsonLoggerAdapter(Printer):
    logger: JsonLogger

    def print(self, message: str) -> None:
        self.logger.write_json(f'{{"message":"{message}"}}')


JsonLoggerAdapter(JsonLogger()).print("build finished")
```

<!-- REGISTRY_PATH: adapter.languages.scala -->
### scala

```scala
// Adapter
trait Printer {
    def printText(text: String): Unit
}

case class TextPrinter() extends Printer {
    def printText(text: String): Unit = println(s"Printing: $text")
}

class JSONObject(val data: Map[String, String])

class JSONToPrinterAdapter(json: JSONObject) extends Printer {
    def printText(text: String): Unit = {
        println(s"Adapted JSON: ${json.data.toString()}")
    }
}

object Main extends App {
    val textPrinter: Printer = TextPrinter()
    textPrinter.printText("Hello")
    
    val json = JSONObject(Map("key" -> "value"))
    val adaptedPrinter: Printer = JSONToPrinterAdapter(json)
    adaptedPrinter.printText("")
}
```

<!-- REGISTRY_PATH: adapter.languages.typescript -->
### typescript

```typescript
interface Printer {
  print(message: string): void;
}

class JsonLogger {
  writeJson(payload: string): void {
    console.log(payload);
  }
}

class JsonLoggerAdapter implements Printer {
  constructor(private readonly logger: JsonLogger) {}

  print(message: string): void {
    this.logger.writeJson(`{"message":"${message}"}`);
  }
}

new JsonLoggerAdapter(new JsonLogger()).print('build finished');
```

## bridge

- Docs: /legacy_content/docs/design_pattern/bridge/README.md

<!-- REGISTRY_PATH: bridge.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>
#include <string>

struct Sender {
    virtual ~Sender() = default;
    virtual void send(const std::string& message) const = 0;
};

struct EmailSender : Sender {
    void send(const std::string& message) const override {
        std::cout << "email: " << message << '\n';
    }
};

struct SmsSender : Sender {
    void send(const std::string& message) const override {
        std::cout << "sms: " << message << '\n';
    }
};

class Notification {
public:
    explicit Notification(const Sender& sender) : sender_(sender) {}
    virtual ~Notification() = default;
    virtual void notify(const std::string& message) const = 0;

protected:
    const Sender& sender_;
};

class AlertNotification : public Notification {
public:
    using Notification::Notification;

    void notify(const std::string& message) const override {
        sender_.send("alert -> " + message);
    }
};

int main() {
    EmailSender email;
    SmsSender sms;
    AlertNotification(email).notify("CPU high");
    AlertNotification(sms).notify("CPU high");
}
```

<!-- REGISTRY_PATH: bridge.languages.go -->
### go

```go
package main

import "fmt"

type Sender interface {
	Send(message string)
}

type EmailSender struct{}

func (EmailSender) Send(message string) {
	fmt.Println("email:", message)
}

type SMSSender struct{}

func (SMSSender) Send(message string) {
	fmt.Println("sms:", message)
}

type AlertNotification struct {
	sender Sender
}

func (n AlertNotification) Notify(message string) {
	n.sender.Send("alert -> " + message)
}

func main() {
	AlertNotification{sender: EmailSender{}}.Notify("CPU high")
	AlertNotification{sender: SMSSender{}}.Notify("CPU high")
}
```

<!-- REGISTRY_PATH: bridge.languages.python -->
### python

```python
from dataclasses import dataclass
from typing import Protocol


class Sender(Protocol):
    def send(self, message: str) -> None: ...


class EmailSender:
    def send(self, message: str) -> None:
        print(f"email: {message}")


class SmsSender:
    def send(self, message: str) -> None:
        print(f"sms: {message}")


@dataclass
class AlertNotification:
    sender: Sender

    def notify(self, message: str) -> None:
        self.sender.send(f"alert -> {message}")


AlertNotification(EmailSender()).notify("CPU high")
AlertNotification(SmsSender()).notify("CPU high")
```

<!-- REGISTRY_PATH: bridge.languages.scala -->
### scala

```scala
// Bridge
trait Sender {
    def send(msg: String): Unit
}

case class EmailSender() extends Sender {
    def send(msg: String): Unit = println(s"Email: $msg")
}

case class SMSSender() extends Sender {
    def send(msg: String): Unit = println(s"SMS: $msg")
}

abstract class Notification(sender: Sender) {
    def notify(msg: String): Unit = sender.send(msg)
}

class Alert(sender: Sender) extends Notification(sender)

object Main extends App {
    val emailSender = EmailSender()
    val smsSender = SMSSender()
    
    val emailAlert = new Alert(emailSender)
    val smsAlert = new Alert(smsSender)
    
    emailAlert.notify("Test alert")
    smsAlert.notify("Test alert")
}
```

<!-- REGISTRY_PATH: bridge.languages.typescript -->
### typescript

```typescript
interface Sender {
  send(message: string): void;
}

class EmailSender implements Sender {
  send(message: string): void {
    console.log(`email: ${message}`);
  }
}

class SmsSender implements Sender {
  send(message: string): void {
    console.log(`sms: ${message}`);
  }
}

class AlertNotification {
  constructor(private readonly sender: Sender) {}

  notify(message: string): void {
    this.sender.send(`alert -> ${message}`);
  }
}

new AlertNotification(new EmailSender()).notify('CPU high');
new AlertNotification(new SmsSender()).notify('CPU high');
```

## builder

- Docs: /legacy_content/docs/design_pattern/builder/README.md

<!-- REGISTRY_PATH: builder.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>
#include <utility>
#include <vector>

struct Report {
    std::string title;
    std::vector<std::string> sections;
};

class ReportBuilder {
public:
    ReportBuilder& title(std::string value) {
        report_.title = std::move(value);
        return *this;
    }

    ReportBuilder& section(std::string value) {
        report_.sections.push_back(std::move(value));
        return *this;
    }

    Report build() {
        return report_;
    }

private:
    Report report_;
};

int main() {
    Report report = ReportBuilder()
        .title("Daily Build")
        .section("tests: green")
        .section("deploy: staged")
        .build();

    std::cout << report.title << '\n';
    for (const auto& section : report.sections) {
        std::cout << "- " << section << '\n';
    }
}
```

<!-- REGISTRY_PATH: builder.languages.go -->
### go

```go
package main

import "fmt"

type Report struct {
	Title    string
	Sections []string
}

type ReportBuilder struct {
	report Report
}

func (b *ReportBuilder) Title(value string) *ReportBuilder {
	b.report.Title = value
	return b
}

func (b *ReportBuilder) Section(value string) *ReportBuilder {
	b.report.Sections = append(b.report.Sections, value)
	return b
}

func (b *ReportBuilder) Build() Report {
	return b.report
}

func main() {
	report := (&ReportBuilder{}).
		Title("Daily Build").
		Section("tests: green").
		Section("deploy: staged").
		Build()

	fmt.Println(report.Title)
	for _, section := range report.Sections {
		fmt.Println("-", section)
	}
}
```

<!-- REGISTRY_PATH: builder.languages.python -->
### python

```python
from dataclasses import dataclass, field


@dataclass
class Report:
    title: str = ""
    sections: list[str] = field(default_factory=list)


class ReportBuilder:
    def __init__(self) -> None:
        self._report = Report()

    def title(self, value: str) -> "ReportBuilder":
        self._report.title = value
        return self

    def section(self, value: str) -> "ReportBuilder":
        self._report.sections.append(value)
        return self

    def build(self) -> Report:
        return self._report


report = (
    ReportBuilder()
    .title("Daily Build")
    .section("tests: green")
    .section("deploy: staged")
    .build()
)

print(report.title)
for section in report.sections:
    print(f"- {section}")
```

<!-- REGISTRY_PATH: builder.languages.scala -->
### scala

```scala
// Builder
case class House(
    walls: String = "",
    roof: String = "",
    windows: Int = 0,
    doors: Int = 0
)

class HouseBuilder {
    private var walls: String = ""
    private var roof: String = ""
    private var windows: Int = 0
    private var doors: Int = 0

    def withWalls(w: String): HouseBuilder = {
        walls = w
        this
    }

    def withRoof(r: String): HouseBuilder = {
        roof = r
        this
    }

    def withWindows(w: Int): HouseBuilder = {
        windows = w
        this
    }

    def withDoors(d: Int): HouseBuilder = {
        doors = d
        this
    }

    def build(): House = House(walls, roof, windows, doors)
}

object Main extends App {
    val house = new HouseBuilder()
        .withWalls("Wood")
        .withRoof("Shingles")
        .withWindows(8)
        .withDoors(2)
        .build()

    println(house)
}
```

<!-- REGISTRY_PATH: builder.languages.typescript -->
### typescript

```typescript
type Report = {
  title: string;
  sections: string[];
};

class ReportBuilder {
  private report: Report = { title: '', sections: [] };

  title(value: string): this {
    this.report.title = value;
    return this;
  }

  section(value: string): this {
    this.report.sections.push(value);
    return this;
  }

  build(): Report {
    return this.report;
  }
}

const report = new ReportBuilder()
  .title('Daily Build')
  .section('tests: green')
  .section('deploy: staged')
  .build();

console.log(report.title);
for (const section of report.sections) {
  console.log(`- ${section}`);
}
```

## chain_of_responsibility

- Docs: /legacy_content/docs/design_pattern/chain_of_responsibility/README.md

<!-- REGISTRY_PATH: chain_of_responsibility.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>
#include <string>

class Request {
public:
    int level;
    std::string message;
    Request(int l, const std::string& m) : level(l), message(m) {}
};

class Handler {
protected:
    std::shared_ptr<Handler> next;
public:
    void setNext(std::shared_ptr<Handler> handler) { next = handler; }
    virtual void handle(const Request& req) = 0;
};

class LowLevelHandler : public Handler {
public:
    void handle(const Request& req) override {
        if (req.level <= 1) {
            std::cout << "LowLevelHandler: Processing " << req.message << std::endl;
        } else if (next) {
            next->handle(req);
        }
    }
};

class MidLevelHandler : public Handler {
public:
    void handle(const Request& req) override {
        if (req.level == 2) {
            std::cout << "MidLevelHandler: Processing " << req.message << std::endl;
        } else if (next) {
            next->handle(req);
        }
    }
};

class HighLevelHandler : public Handler {
public:
    void handle(const Request& req) override {
        if (req.level >= 3) {
            std::cout << "HighLevelHandler: Processing " << req.message << std::endl;
        }
    }
};

int main() {
    auto low = std::make_shared<LowLevelHandler>();
    auto mid = std::make_shared<MidLevelHandler>();
    auto high = std::make_shared<HighLevelHandler>();
    
    low->setNext(mid);
    mid->setNext(high);
    
    Request r1(1, "Simple request");
    Request r2(2, "Normal request");
    Request r3(3, "Critical request");
    
    low->handle(r1);
    low->handle(r2);
    low->handle(r3);
}
```

<!-- REGISTRY_PATH: chain_of_responsibility.languages.go -->
### go

```go
package main

import (
	"fmt"
)

type Request struct {
	level   int
	message string
}

type Handler interface {
	SetNext(Handler)
	Handle(*Request)
}

type AbstractHandler struct {
	next Handler
}

func (h *AbstractHandler) SetNext(next Handler) {
	h.next = next
}

type LowHandler struct {
	AbstractHandler
}

func (h *LowHandler) Handle(req *Request) {
	if req.level <= 1 {
		fmt.Printf("LowHandler: Processing %s\n", req.message)
	} else if h.next != nil {
		h.next.Handle(req)
	}
}

type MidHandler struct {
	AbstractHandler
}

func (h *MidHandler) Handle(req *Request) {
	if req.level == 2 {
		fmt.Printf("MidHandler: Processing %s\n", req.message)
	} else if h.next != nil {
		h.next.Handle(req)
	}
}

type HighHandler struct {
	AbstractHandler
}

func (h *HighHandler) Handle(req *Request) {
	if req.level >= 3 {
		fmt.Printf("HighHandler: Processing %s\n", req.message)
	}
}

func main() {
	low := &LowHandler{}
	mid := &MidHandler{}
	high := &HighHandler{}

	low.SetNext(mid)
	mid.SetNext(high)

	low.Handle(&Request{1, "Simple"})
	low.Handle(&Request{2, "Normal"})
	low.Handle(&Request{3, "Critical"})
}
```

<!-- REGISTRY_PATH: chain_of_responsibility.languages.python -->
### python

```python
from abc import ABC, abstractmethod
from typing import Optional

class Request:
    def __init__(self, level: int, message: str):
        self.level = level
        self.message = message

class Handler(ABC):
    def __init__(self):
        self.next: Optional[Handler] = None
    
    def set_next(self, handler: "Handler") -> "Handler":
        self.next = handler
        return handler
    
    @abstractmethod
    def handle(self, request: Request) -> str:
        pass

class LowHandler(Handler):
    def handle(self, request: Request) -> str:
        if request.level <= 1:
            return f"LowHandler: {request.message}"
        return self.next.handle(request) if self.next else ""

class MidHandler(Handler):
    def handle(self, request: Request) -> str:
        if request.level == 2:
            return f"MidHandler: {request.message}"
        return self.next.handle(request) if self.next else ""

class HighHandler(Handler):
    def handle(self, request: Request) -> str:
        if request.level >= 3:
            return f"HighHandler: {request.message}"
        return ""

low = LowHandler()
mid = MidHandler()
high = HighHandler()

low.set_next(mid).set_next(high)

print(low.handle(Request(1, "Simple")))
print(low.handle(Request(2, "Normal")))
print(low.handle(Request(3, "Critical")))
```

<!-- REGISTRY_PATH: chain_of_responsibility.languages.scala -->
### scala

```scala
// Chain of Responsibility
case class Request(level: Int, message: String)

trait Handler {
    protected var next: Option[Handler] = None
    
    def setNext(h: Handler): Handler = {
        next = Some(h)
        h
    }
    
    def handle(req: Request): Unit
}

class LowHandler extends Handler {
    def handle(req: Request): Unit = {
        if (req.level <= 1) {
            println(s"LowHandler: ${req.message}")
        } else {
            next.foreach(_.handle(req))
        }
    }
}

class MidHandler extends Handler {
    def handle(req: Request): Unit = {
        if (req.level == 2) {
            println(s"MidHandler: ${req.message}")
        } else {
            next.foreach(_.handle(req))
        }
    }
}

class HighHandler extends Handler {
    def handle(req: Request): Unit = {
        if (req.level >= 3) {
            println(s"HighHandler: ${req.message}")
        }
    }
}

object Main extends App {
    val low = new LowHandler()
    val mid = new MidHandler()
    val high = new HighHandler()
    
    low.setNext(mid).setNext(high)
    
    low.handle(Request(1, "Simple"))
    low.handle(Request(2, "Normal"))
    low.handle(Request(3, "Critical"))
}
```

<!-- REGISTRY_PATH: chain_of_responsibility.languages.typescript -->
### typescript

```typescript
interface IHandler {
    setNext(next: IHandler): void;
    handle(request: Request): void;
}

class Request {
    constructor(public level: number, public message: string) {}
}

abstract class BaseHandler implements IHandler {
    protected next: IHandler | null = null;
    
    setNext(next: IHandler): void {
        this.next = next;
    }
    
    abstract handle(request: Request): void;
}

class LowHandler extends BaseHandler {
    handle(request: Request): void {
        if (request.level <= 1) {
            console.log(`LowHandler: ${request.message}`);
        } else if (this.next) {
            this.next.handle(request);
        }
    }
}

class MidHandler extends BaseHandler {
    handle(request: Request): void {
        if (request.level === 2) {
            console.log(`MidHandler: ${request.message}`);
        } else if (this.next) {
            this.next.handle(request);
        }
    }
}

class HighHandler extends BaseHandler {
    handle(request: Request): void {
        if (request.level >= 3) {
            console.log(`HighHandler: ${request.message}`);
        }
    }
}

const low = new LowHandler();
const mid = new MidHandler();
const high = new HighHandler();

low.setNext(mid);
mid.setNext(high);

low.handle(new Request(1, "Simple"));
low.handle(new Request(2, "Normal"));
low.handle(new Request(3, "Critical"));
```

## command

- Docs: /legacy_content/docs/design_pattern/command/README.md

<!-- REGISTRY_PATH: command.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>
#include <vector>

class Receiver {
public:
    void turnOn() { std::cout << "Device is ON\n"; }
    void turnOff() { std::cout << "Device is OFF\n"; }
};

class Command {
public:
    virtual ~Command() = default;
    virtual void execute() = 0;
};

class TurnOnCommand : public Command {
private:
    std::shared_ptr<Receiver> receiver;
public:
    TurnOnCommand(std::shared_ptr<Receiver> r) : receiver(r) {}
    void execute() override { receiver->turnOn(); }
};

class TurnOffCommand : public Command {
private:
    std::shared_ptr<Receiver> receiver;
public:
    TurnOffCommand(std::shared_ptr<Receiver> r) : receiver(r) {}
    void execute() override { receiver->turnOff(); }
};

class Invoker {
private:
    std::vector<std::shared_ptr<Command>> commands;
public:
    void addCommand(std::shared_ptr<Command> cmd) { commands.push_back(cmd); }
    void executeAll() {
        for (auto& cmd : commands) {
            cmd->execute();
        }
    }
};

int main() {
    auto device = std::make_shared<Receiver>();
    auto invoker = std::make_unique<Invoker>();
    
    invoker->addCommand(std::make_shared<TurnOnCommand>(device));
    invoker->addCommand(std::make_shared<TurnOffCommand>(device));
    
    invoker->executeAll();
}
```

<!-- REGISTRY_PATH: command.languages.go -->
### go

```go
package main

import "fmt"

type Receiver struct{}

func (r *Receiver) TurnOn() {
	fmt.Println("Device is ON")
}

func (r *Receiver) TurnOff() {
	fmt.Println("Device is OFF")
}

type Command interface {
	Execute()
}

type TurnOnCommand struct {
	receiver *Receiver
}

func (c *TurnOnCommand) Execute() {
	c.receiver.TurnOn()
}

type TurnOffCommand struct {
	receiver *Receiver
}

func (c *TurnOffCommand) Execute() {
	c.receiver.TurnOff()
}

type Invoker struct {
	commands []Command
}

func (i *Invoker) AddCommand(cmd Command) {
	i.commands = append(i.commands, cmd)
}

func (i *Invoker) ExecuteAll() {
	for _, cmd := range i.commands {
		cmd.Execute()
	}
}

func main() {
	device := &Receiver{}
	invoker := &Invoker{}

	invoker.AddCommand(&TurnOnCommand{device})
	invoker.AddCommand(&TurnOffCommand{device})

	invoker.ExecuteAll()
}
```

<!-- REGISTRY_PATH: command.languages.python -->
### python

```python
from abc import ABC, abstractmethod

class Receiver:
    def turn_on(self):
        print("Device is ON")
    
    def turn_off(self):
        print("Device is OFF")

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class TurnOnCommand(Command):
    def __init__(self, receiver: Receiver):
        self.receiver = receiver
    
    def execute(self) -> None:
        self.receiver.turn_on()

class TurnOffCommand(Command):
    def __init__(self, receiver: Receiver):
        self.receiver = receiver
    
    def execute(self) -> None:
        self.receiver.turn_off()

class Invoker:
    def __init__(self):
        self.commands: list[Command] = []
    
    def add_command(self, command: Command) -> None:
        self.commands.append(command)
    
    def execute_all(self) -> None:
        for cmd in self.commands:
            cmd.execute()

device = Receiver()
invoker = Invoker()

invoker.add_command(TurnOnCommand(device))
invoker.add_command(TurnOffCommand(device))

invoker.execute_all()
```

<!-- REGISTRY_PATH: command.languages.scala -->
### scala

```scala
// Command
class Device {
    def turnOn(): Unit = println("Device is ON")
    def turnOff(): Unit = println("Device is OFF")
}

trait Command {
    def execute(): Unit
}

class TurnOnCommand(device: Device) extends Command {
    def execute(): Unit = device.turnOn()
}

class TurnOffCommand(device: Device) extends Command {
    def execute(): Unit = device.turnOff()
}

class Invoker {
    private var commands: List[Command] = List()
    
    def addCommand(cmd: Command): Unit = {
        commands = commands :+ cmd
    }
    
    def executeAll(): Unit = {
        commands.foreach(_.execute())
    }
}

object Main extends App {
    val device = new Device()
    val invoker = new Invoker()
    
    invoker.addCommand(new TurnOnCommand(device))
    invoker.addCommand(new TurnOffCommand(device))
    
    invoker.executeAll()
}
```

<!-- REGISTRY_PATH: command.languages.typescript -->
### typescript

```typescript
interface ICommand {
    execute(): void;
}

class Receiver {
    turnOn(): void {
        console.log("Device is ON");
    }
    
    turnOff(): void {
        console.log("Device is OFF");
    }
}

class TurnOnCommand implements ICommand {
    constructor(private receiver: Receiver) {}
    
    execute(): void {
        this.receiver.turnOn();
    }
}

class TurnOffCommand implements ICommand {
    constructor(private receiver: Receiver) {}
    
    execute(): void {
        this.receiver.turnOff();
    }
}

class Invoker {
    private commands: ICommand[] = [];
    
    addCommand(command: ICommand): void {
        this.commands.push(command);
    }
    
    executeAll(): void {
        for (const cmd of this.commands) {
            cmd.execute();
        }
    }
}

const device = new Receiver();
const invoker = new Invoker();

invoker.addCommand(new TurnOnCommand(device));
invoker.addCommand(new TurnOffCommand(device));

invoker.executeAll();
```

## composite

- Docs: /legacy_content/docs/design_pattern/composite/README.md

<!-- REGISTRY_PATH: composite.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>
#include <numeric>
#include <vector>

struct Node {
    virtual ~Node() = default;
    virtual int totalSize() const = 0;
};

struct File : Node {
    explicit File(int size) : size_(size) {}
    int totalSize() const override { return size_; }
    int size_;
};

class Folder : public Node {
public:
    void add(std::unique_ptr<Node> child) {
        children_.push_back(std::move(child));
    }

    int totalSize() const override {
        int sum = 0;
        for (const auto& child : children_) {
            sum += child->totalSize();
        }
        return sum;
    }

private:
    std::vector<std::unique_ptr<Node>> children_;
};

int main() {
    auto root = std::make_unique<Folder>();
    root->add(std::make_unique<File>(5));
    auto sub = std::make_unique<Folder>();
    sub->add(std::make_unique<File>(7));
    sub->add(std::make_unique<File>(3));
    root->add(std::move(sub));
    std::cout << root->totalSize() << '\n';
}
```

<!-- REGISTRY_PATH: composite.languages.go -->
### go

```go
package main

import "fmt"

type Node interface {
	TotalSize() int
}

type File struct {
	size int
}

func (f File) TotalSize() int { return f.size }

type Folder struct {
	children []Node
}

func (f *Folder) Add(child Node) {
	f.children = append(f.children, child)
}

func (f Folder) TotalSize() int {
	total := 0
	for _, child := range f.children {
		total += child.TotalSize()
	}
	return total
}

func main() {
	root := &Folder{}
	root.Add(File{size: 5})
	sub := &Folder{}
	sub.Add(File{size: 7})
	sub.Add(File{size: 3})
	root.Add(sub)
	fmt.Println(root.TotalSize())
}
```

<!-- REGISTRY_PATH: composite.languages.python -->
### python

```python
from dataclasses import dataclass, field
from typing import Protocol


class Node(Protocol):
    def total_size(self) -> int: ...


@dataclass
class File:
    size: int

    def total_size(self) -> int:
        return self.size


@dataclass
class Folder:
    children: list[Node] = field(default_factory=list)

    def add(self, child: Node) -> None:
        self.children.append(child)

    def total_size(self) -> int:
        return sum(child.total_size() for child in self.children)


root = Folder()
root.add(File(5))
sub = Folder([File(7), File(3)])
root.add(sub)
print(root.total_size())
```

<!-- REGISTRY_PATH: composite.languages.scala -->
### scala

```scala
// Composite
trait FileSystemNode {
    def getSize(): Long
}

case class File(name: String, size: Long) extends FileSystemNode {
    def getSize(): Long = size
}

class Folder(name: String) extends FileSystemNode {
    private var children: List[FileSystemNode] = List()
    
    def add(node: FileSystemNode): Unit = {
        children = children :+ node
    }
    
    def getSize(): Long = children.map(_.getSize()).sum
}

object Main extends App {
    val file1 = File("file1.txt", 100)
    val file2 = File("file2.txt", 200)
    
    val folder = new Folder("documents")
    folder.add(file1)
    folder.add(file2)
    
    println(s"Folder size: ${folder.getSize()}")
}
```

<!-- REGISTRY_PATH: composite.languages.typescript -->
### typescript

```typescript
interface Node {
  totalSize(): number;
}

class FileNode implements Node {
  constructor(private readonly size: number) {}

  totalSize(): number {
    return this.size;
  }
}

class Folder implements Node {
  private readonly children: Node[] = [];

  add(child: Node): void {
    this.children.push(child);
  }

  totalSize(): number {
    return this.children.reduce((sum, child) => sum + child.totalSize(), 0);
  }
}

const root = new Folder();
root.add(new FileNode(5));
const sub = new Folder();
sub.add(new FileNode(7));
sub.add(new FileNode(3));
root.add(sub);
console.log(root.totalSize());
```

## decorator

- Docs: /legacy_content/docs/design_pattern/decorator/README.md

<!-- REGISTRY_PATH: decorator.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>
#include <string>

struct Notifier {
    virtual ~Notifier() = default;
    virtual void send(const std::string& message) const = 0;
};

struct EmailNotifier : Notifier {
    void send(const std::string& message) const override {
        std::cout << "email: " << message << '\n';
    }
};

class NotifierDecorator : public Notifier {
public:
    explicit NotifierDecorator(std::unique_ptr<Notifier> inner) : inner_(std::move(inner)) {}

protected:
    std::unique_ptr<Notifier> inner_;
};

class SmsDecorator : public NotifierDecorator {
public:
    using NotifierDecorator::NotifierDecorator;

    void send(const std::string& message) const override {
        inner_->send(message);
        std::cout << "sms: " << message << '\n';
    }
};

int main() {
    auto notifier = std::make_unique<SmsDecorator>(std::make_unique<EmailNotifier>());
    notifier->send("deployment done");
}
```

<!-- REGISTRY_PATH: decorator.languages.go -->
### go

```go
package main

import "fmt"

type Notifier interface {
	Send(message string)
}

type EmailNotifier struct{}

func (EmailNotifier) Send(message string) {
	fmt.Println("email:", message)
}

type SMSDecorator struct {
	inner Notifier
}

func (d SMSDecorator) Send(message string) {
	d.inner.Send(message)
	fmt.Println("sms:", message)
}

func main() {
	notifier := SMSDecorator{inner: EmailNotifier{}}
	notifier.Send("deployment done")
}
```

<!-- REGISTRY_PATH: decorator.languages.python -->
### python

```python
from dataclasses import dataclass
from typing import Protocol


class Notifier(Protocol):
    def send(self, message: str) -> None: ...


class EmailNotifier:
    def send(self, message: str) -> None:
        print(f"email: {message}")


@dataclass
class SmsDecorator:
    inner: Notifier

    def send(self, message: str) -> None:
        self.inner.send(message)
        print(f"sms: {message}")


SmsDecorator(EmailNotifier()).send("deployment done")
```

<!-- REGISTRY_PATH: decorator.languages.scala -->
### scala

```scala
// Decorator
trait Notification {
    def send(): Unit
}

class BasicNotification extends Notification {
    def send(): Unit = print("Sending notification")
}

class EmailNotification(notif: Notification) extends Notification {
    def send(): Unit = {
        notif.send()
        print(" + Email")
    }
}

class SMSNotification(notif: Notification) extends Notification {
    def send(): Unit = {
        notif.send()
        print(" + SMS")
    }
}

object Main extends App {
    var notif: Notification = new BasicNotification()
    notif = new EmailNotification(notif)
    notif = new SMSNotification(notif)
    
    notif.send()
    println()
}
```

<!-- REGISTRY_PATH: decorator.languages.typescript -->
### typescript

```typescript
interface Notifier {
  send(message: string): void;
}

class EmailNotifier implements Notifier {
  send(message: string): void {
    console.log(`email: ${message}`);
  }
}

class SmsDecorator implements Notifier {
  constructor(private readonly inner: Notifier) {}

  send(message: string): void {
    this.inner.send(message);
    console.log(`sms: ${message}`);
  }
}

new SmsDecorator(new EmailNotifier()).send('deployment done');
```

## facade

- Docs: /legacy_content/docs/design_pattern/facade/README.md

<!-- REGISTRY_PATH: facade.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>

struct Compiler {
    void run() const { std::cout << "compile\n"; }
};

struct TestRunner {
    void run() const { std::cout << "test\n"; }
};

struct Packager {
    void run() const { std::cout << "package\n"; }
};

class ReleaseFacade {
public:
    void deploy() const {
        compiler_.run();
        tests_.run();
        packager_.run();
    }

private:
    Compiler compiler_;
    TestRunner tests_;
    Packager packager_;
};

int main() {
    ReleaseFacade().deploy();
}
```

<!-- REGISTRY_PATH: facade.languages.go -->
### go

```go
package main

import "fmt"

type Compiler struct{}

func (Compiler) Run() { fmt.Println("compile") }

type TestRunner struct{}

func (TestRunner) Run() { fmt.Println("test") }

type Packager struct{}

func (Packager) Run() { fmt.Println("package") }

type ReleaseFacade struct {
	compiler Compiler
	tests    TestRunner
	packager Packager
}

func (f ReleaseFacade) Deploy() {
	f.compiler.Run()
	f.tests.Run()
	f.packager.Run()
}

func main() {
	ReleaseFacade{}.Deploy()
}
```

<!-- REGISTRY_PATH: facade.languages.python -->
### python

```python
class Compiler:
    def run(self) -> None:
        print("compile")


class TestRunner:
    def run(self) -> None:
        print("test")


class Packager:
    def run(self) -> None:
        print("package")


class ReleaseFacade:
    def __init__(self) -> None:
        self.compiler = Compiler()
        self.tests = TestRunner()
        self.packager = Packager()

    def deploy(self) -> None:
        self.compiler.run()
        self.tests.run()
        self.packager.run()


ReleaseFacade().deploy()
```

<!-- REGISTRY_PATH: facade.languages.scala -->
### scala

```scala
// Facade
class Compiler {
    def compile(): Unit = println("Compiling code...")
}

class Tester {
    def test(): Unit = println("Running tests...")
}

class Deployer {
    def deploy(): Unit = println("Deploying package...")
}

class BuildFacade {
    private val compiler = new Compiler()
    private val tester = new Tester()
    private val deployer = new Deployer()
    
    def build(): Unit = {
        compiler.compile()
        tester.test()
        deployer.deploy()
    }
}

object Main extends App {
    val facade = new BuildFacade()
    facade.build()
}
```

<!-- REGISTRY_PATH: facade.languages.typescript -->
### typescript

```typescript
class Compiler {
  run(): void {
    console.log('compile');
  }
}

class TestRunner {
  run(): void {
    console.log('test');
  }
}

class Packager {
  run(): void {
    console.log('package');
  }
}

class ReleaseFacade {
  private readonly compiler = new Compiler();
  private readonly tests = new TestRunner();
  private readonly packager = new Packager();

  deploy(): void {
    this.compiler.run();
    this.tests.run();
    this.packager.run();
  }
}

new ReleaseFacade().deploy();
```

## factory_method

- Docs: /legacy_content/docs/design_pattern/factory_method/README.md

<!-- REGISTRY_PATH: factory_method.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>
#include <string>

struct Parser {
    virtual ~Parser() = default;
    virtual std::string parse() const = 0;
};

struct JsonParser : Parser {
    std::string parse() const override { return "parsed json"; }
};

struct CsvParser : Parser {
    std::string parse() const override { return "parsed csv"; }
};

class ImportJob {
public:
    virtual ~ImportJob() = default;
    std::string run() const {
        return createParser()->parse();
    }

private:
    virtual std::unique_ptr<Parser> createParser() const = 0;
};

class JsonImportJob : public ImportJob {
private:
    std::unique_ptr<Parser> createParser() const override { return std::make_unique<JsonParser>(); }
};

class CsvImportJob : public ImportJob {
private:
    std::unique_ptr<Parser> createParser() const override { return std::make_unique<CsvParser>(); }
};

int main() {
    JsonImportJob json;
    CsvImportJob csv;
    std::cout << json.run() << '\n';
    std::cout << csv.run() << '\n';
}
```

<!-- REGISTRY_PATH: factory_method.languages.go -->
### go

```go
package main

import "fmt"

type Parser interface{ Parse() string }

type JSONParser struct{}

func (JSONParser) Parse() string { return "parsed json" }

type CSVParser struct{}

func (CSVParser) Parse() string { return "parsed csv" }

type ImportJob interface {
	Run() string
	createParser() Parser
}

type JSONImportJob struct{}

func (JSONImportJob) createParser() Parser { return JSONParser{} }
func (j JSONImportJob) Run() string        { return j.createParser().Parse() }

type CSVImportJob struct{}

func (CSVImportJob) createParser() Parser { return CSVParser{} }
func (j CSVImportJob) Run() string        { return j.createParser().Parse() }

func main() {
	jobs := []ImportJob{JSONImportJob{}, CSVImportJob{}}
	for _, job := range jobs {
		fmt.Println(job.Run())
	}
}
```

<!-- REGISTRY_PATH: factory_method.languages.python -->
### python

```python
from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def parse(self) -> str: ...


class JsonParser(Parser):
    def parse(self) -> str:
        return "parsed json"


class CsvParser(Parser):
    def parse(self) -> str:
        return "parsed csv"


class ImportJob(ABC):
    def run(self) -> str:
        return self.create_parser().parse()

    @abstractmethod
    def create_parser(self) -> Parser: ...


class JsonImportJob(ImportJob):
    def create_parser(self) -> Parser:
        return JsonParser()


class CsvImportJob(ImportJob):
    def create_parser(self) -> Parser:
        return CsvParser()


for job in (JsonImportJob(), CsvImportJob()):
    print(job.run())
```

<!-- REGISTRY_PATH: factory_method.languages.scala -->
### scala

```scala
// Factory Method
trait Vehicle {
    def drive(): String
}

case class Car() extends Vehicle {
    def drive(): String = "Driving a car on road"
}

case class Truck() extends Vehicle {
    def drive(): String = "Driving a truck on highway"
}

trait Factory {
    def createVehicle(): Vehicle
}

object CarFactory extends Factory {
    def createVehicle(): Vehicle = Car()
}

object TruckFactory extends Factory {
    def createVehicle(): Vehicle = Truck()
}

object Main extends App {
    val carFactory: Factory = CarFactory
    val truckFactory: Factory = TruckFactory
    
    println(carFactory.createVehicle().drive())
    println(truckFactory.createVehicle().drive())
}
```

<!-- REGISTRY_PATH: factory_method.languages.typescript -->
### typescript

```typescript
interface Parser {
  parse(): string;
}

class JsonParser implements Parser {
  parse(): string {
    return 'parsed json';
  }
}

class CsvParser implements Parser {
  parse(): string {
    return 'parsed csv';
  }
}

abstract class ImportJob {
  run(): string {
    return this.createParser().parse();
  }

  protected abstract createParser(): Parser;
}

class JsonImportJob extends ImportJob {
  protected createParser(): Parser {
    return new JsonParser();
  }
}

class CsvImportJob extends ImportJob {
  protected createParser(): Parser {
    return new CsvParser();
  }
}

for (const job of [new JsonImportJob(), new CsvImportJob()]) {
  console.log(job.run());
}
```

## flyweight

- Docs: /legacy_content/docs/design_pattern/flyweight/README.md

<!-- REGISTRY_PATH: flyweight.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>
#include <string>
#include <unordered_map>

struct GlyphStyle {
    explicit GlyphStyle(std::string font) : font(std::move(font)) {}
    std::string font;
};

class StyleFactory {
public:
    const GlyphStyle* get(const std::string& font) {
        auto it = styles_.find(font);
        if (it == styles_.end()) {
            it = styles_.emplace(font, std::make_unique<GlyphStyle>(font)).first;
        }
        return it->second.get();
    }

private:
    std::unordered_map<std::string, std::unique_ptr<GlyphStyle>> styles_;
};

int main() {
    StyleFactory factory;
    const GlyphStyle* first = factory.get("mono-12");
    const GlyphStyle* second = factory.get("mono-12");
    std::cout << std::boolalpha << (first == second) << '\n';
}
```

<!-- REGISTRY_PATH: flyweight.languages.go -->
### go

```go
package main

import "fmt"

type GlyphStyle struct {
	font string
}

type StyleFactory struct {
	styles map[string]*GlyphStyle
}

func NewStyleFactory() *StyleFactory {
	return &StyleFactory{styles: map[string]*GlyphStyle{}}
}

func (f *StyleFactory) Get(font string) *GlyphStyle {
	if style, ok := f.styles[font]; ok {
		return style
	}
	style := &GlyphStyle{font: font}
	f.styles[font] = style
	return style
}

func main() {
	factory := NewStyleFactory()
	first := factory.Get("mono-12")
	second := factory.Get("mono-12")
	fmt.Println(first == second)
}
```

<!-- REGISTRY_PATH: flyweight.languages.python -->
### python

```python
class GlyphStyle:
    def __init__(self, font: str) -> None:
        self.font = font


class StyleFactory:
    def __init__(self) -> None:
        self._styles: dict[str, GlyphStyle] = {}

    def get(self, font: str) -> GlyphStyle:
        if font not in self._styles:
            self._styles[font] = GlyphStyle(font)
        return self._styles[font]


factory = StyleFactory()
first = factory.get("mono-12")
second = factory.get("mono-12")
print(first is second)
```

<!-- REGISTRY_PATH: flyweight.languages.scala -->
### scala

```scala
// Flyweight
case class GlyphStyle(font: String, size: Int)

class Glyph(char: Char, style: GlyphStyle) {
    def render(): Unit = println(s"$char in ${style.font}")
}

class GlyphFactory {
    private var cache: Map[GlyphStyle, GlyphStyle] = Map()
    
    def getStyle(font: String, size: Int): GlyphStyle = {
        val key = GlyphStyle(font, size)
        cache.getOrElse(key, {
            cache = cache + (key -> key)
            key
        })
    }
}

object Main extends App {
    val factory = new GlyphFactory()
    
    val style1 = factory.getStyle("Arial", 12)
    val style2 = factory.getStyle("Arial", 12)
    
    val glyph1 = new Glyph('A', style1)
    val glyph2 = new Glyph('B', style2)
    
    glyph1.render()
    glyph2.render()
}
```

<!-- REGISTRY_PATH: flyweight.languages.typescript -->
### typescript

```typescript
class GlyphStyle {
  constructor(public readonly font: string) {}
}

class StyleFactory {
  private readonly styles = new Map<string, GlyphStyle>();

  get(font: string): GlyphStyle {
    const existing = this.styles.get(font);
    if (existing) {
      return existing;
    }
    const created = new GlyphStyle(font);
    this.styles.set(font, created);
    return created;
  }
}

const factory = new StyleFactory();
const first = factory.get('mono-12');
const second = factory.get('mono-12');
console.log(first === second);
```

## interpreter

- Docs: /legacy_content/docs/design_pattern/interpreter/README.md

<!-- REGISTRY_PATH: interpreter.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>
#include <memory>

class Expression {
public:
    virtual ~Expression() = default;
    virtual bool interpret(const std::string& ctx) = 0;
};

class TerminalExpression : public Expression {
private:
    std::string literal;
public:
    TerminalExpression(const std::string& lit) : literal(lit) {}
    
    bool interpret(const std::string& ctx) override {
        return ctx.find(literal) != std::string::npos;
    }
};

class OrExpression : public Expression {
private:
    std::shared_ptr<Expression> expr1, expr2;
public:
    OrExpression(std::shared_ptr<Expression> e1, std::shared_ptr<Expression> e2)
        : expr1(e1), expr2(e2) {}
    
    bool interpret(const std::string& ctx) override {
        return expr1->interpret(ctx) || expr2->interpret(ctx);
    }
};

class AndExpression : public Expression {
private:
    std::shared_ptr<Expression> expr1, expr2;
public:
    AndExpression(std::shared_ptr<Expression> e1, std::shared_ptr<Expression> e2)
        : expr1(e1), expr2(e2) {}
    
    bool interpret(const std::string& ctx) override {
        return expr1->interpret(ctx) && expr2->interpret(ctx);
    }
};

int main() {
    auto c1 = std::make_shared<TerminalExpression>("cat");
    auto c2 = std::make_shared<TerminalExpression>("dog");
    auto expr = std::make_shared<OrExpression>(c1, c2);
    
    std::cout << (expr->interpret("cat") ? "true" : "false") << std::endl;
    std::cout << (expr->interpret("bird") ? "true" : "false") << std::endl;
}
```

<!-- REGISTRY_PATH: interpreter.languages.go -->
### go

```go
package main

import (
	"fmt"
	"strings"
)

type Expression interface {
	Interpret(string) bool
}

type TerminalExpression struct {
	literal string
}

func (t *TerminalExpression) Interpret(ctx string) bool {
	return strings.Contains(ctx, t.literal)
}

type OrExpression struct {
	expr1, expr2 Expression
}

func (o *OrExpression) Interpret(ctx string) bool {
	return o.expr1.Interpret(ctx) || o.expr2.Interpret(ctx)
}

type AndExpression struct {
	expr1, expr2 Expression
}

func (a *AndExpression) Interpret(ctx string) bool {
	return a.expr1.Interpret(ctx) && a.expr2.Interpret(ctx)
}

func main() {
	c1 := &TerminalExpression{"cat"}
	c2 := &TerminalExpression{"dog"}
	expr := &OrExpression{c1, c2}

	fmt.Println(expr.Interpret("cat"))
	fmt.Println(expr.Interpret("bird"))
}
```

<!-- REGISTRY_PATH: interpreter.languages.python -->
### python

```python
from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self, ctx: str) -> bool:
        pass

class TerminalExpression(Expression):
    def __init__(self, literal: str):
        self.literal = literal
    
    def interpret(self, ctx: str) -> bool:
        return self.literal in ctx

class OrExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def interpret(self, ctx: str) -> bool:
        return self.expr1.interpret(ctx) or self.expr2.interpret(ctx)

class AndExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def interpret(self, ctx: str) -> bool:
        return self.expr1.interpret(ctx) and self.expr2.interpret(ctx)

c1 = TerminalExpression("cat")
c2 = TerminalExpression("dog")
expr = OrExpression(c1, c2)

print(expr.interpret("cat"))
print(expr.interpret("bird"))
```

<!-- REGISTRY_PATH: interpreter.languages.scala -->
### scala

```scala
// Interpreter
trait Expression {
    def interpret(ctx: String): Boolean
}

class TerminalExpression(literal: String) extends Expression {
    def interpret(ctx: String): Boolean = ctx.contains(literal)
}

class OrExpression(expr1: Expression, expr2: Expression) extends Expression {
    def interpret(ctx: String): Boolean = expr1.interpret(ctx) || expr2.interpret(ctx)
}

class AndExpression(expr1: Expression, expr2: Expression) extends Expression {
    def interpret(ctx: String): Boolean = expr1.interpret(ctx) && expr2.interpret(ctx)
}

object Main extends App {
    val c1: Expression = new TerminalExpression("cat")
    val c2: Expression = new TerminalExpression("dog")
    val expr: Expression = new OrExpression(c1, c2)
    
    println(expr.interpret("cat"))
    println(expr.interpret("bird"))
}
```

<!-- REGISTRY_PATH: interpreter.languages.typescript -->
### typescript

```typescript
interface Expression {
    interpret(ctx: string): boolean;
}

class TerminalExpression implements Expression {
    constructor(private literal: string) {}
    
    interpret(ctx: string): boolean {
        return ctx.includes(this.literal);
    }
}

class OrExpression implements Expression {
    constructor(private expr1: Expression, private expr2: Expression) {}
    
    interpret(ctx: string): boolean {
        return this.expr1.interpret(ctx) || this.expr2.interpret(ctx);
    }
}

class AndExpression implements Expression {
    constructor(private expr1: Expression, private expr2: Expression) {}
    
    interpret(ctx: string): boolean {
        return this.expr1.interpret(ctx) && this.expr2.interpret(ctx);
    }
}

const c1 = new TerminalExpression("cat");
const c2 = new TerminalExpression("dog");
const expr = new OrExpression(c1, c2);

console.log(expr.interpret("cat"));
console.log(expr.interpret("bird"));
```

## iterator

- Docs: /legacy_content/docs/design_pattern/iterator/README.md

<!-- REGISTRY_PATH: iterator.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <memory>

template <typename T>
class Iterator {
public:
    virtual ~Iterator() = default;
    virtual bool hasNext() = 0;
    virtual T next() = 0;
};

template <typename T>
class Collection {
public:
    virtual ~Collection() = default;
    virtual std::unique_ptr<Iterator<T>> createIterator() = 0;
};

template <typename T>
class ArrayIterator : public Iterator<T> {
private:
    std::vector<T>& items;
    int position = 0;
public:
    ArrayIterator(std::vector<T>& items) : items(items) {}
    
    bool hasNext() override {
        return position < items.size();
    }
    
    T next() override {
        return items[position++];
    }
};

template <typename T>
class ArrayCollection : public Collection<T> {
private:
    std::vector<T> items;
public:
    void add(T item) { items.push_back(item); }
    
    std::unique_ptr<Iterator<T>> createIterator() override {
        return std::make_unique<ArrayIterator<T>>(items);
    }
};

int main() {
    ArrayCollection<int> collection;
    collection.add(10);
    collection.add(20);
    collection.add(30);
    
    auto it = collection.createIterator();
    while (it->hasNext()) {
        std::cout << it->next() << " ";
    }
    std::cout << std::endl;
}
```

<!-- REGISTRY_PATH: iterator.languages.go -->
### go

```go
package main

import "fmt"

type Iterator interface {
	HasNext() bool
	Next() int
}

type Collection interface {
	CreateIterator() Iterator
}

type ArrayIterator struct {
	items    []int
	position int
}

func (i *ArrayIterator) HasNext() bool {
	return i.position < len(i.items)
}

func (i *ArrayIterator) Next() int {
	result := i.items[i.position]
	i.position++
	return result
}

type ArrayCollection struct {
	items []int
}

func (c *ArrayCollection) Add(item int) {
	c.items = append(c.items, item)
}

func (c *ArrayCollection) CreateIterator() Iterator {
	return &ArrayIterator{c.items, 0}
}

func main() {
	collection := &ArrayCollection{}
	collection.Add(10)
	collection.Add(20)
	collection.Add(30)

	it := collection.CreateIterator()
	for it.HasNext() {
		fmt.Printf("%d ", it.Next())
	}
	fmt.Println()
}
```

<!-- REGISTRY_PATH: iterator.languages.python -->
### python

```python
from abc import ABC, abstractmethod
from typing import Any, Iterator as PyIterator

class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass
    
    @abstractmethod
    def next(self) -> Any:
        pass

class Collection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass

class ArrayIterator(Iterator):
    def __init__(self, items: list):
        self.items = items
        self.position = 0
    
    def has_next(self) -> bool:
        return self.position < len(self.items)
    
    def next(self) -> Any:
        result = self.items[self.position]
        self.position += 1
        return result

class ArrayCollection(Collection):
    def __init__(self):
        self.items = []
    
    def add(self, item: Any) -> None:
        self.items.append(item)
    
    def create_iterator(self) -> Iterator:
        return ArrayIterator(self.items)

collection = ArrayCollection()
collection.add(10)
collection.add(20)
collection.add(30)

it = collection.create_iterator()
while it.has_next():
    print(it.next(), end=" ")
print()
```

<!-- REGISTRY_PATH: iterator.languages.scala -->
### scala

```scala
// Iterator
trait CustomIterator[T] {
    def hasNext: Boolean
    def next(): T
}

trait CustomCollection[T] {
    def createIterator(): CustomIterator[T]
}

class ArrayIterator[T](items: Vector[T]) extends CustomIterator[T] {
    private var position = 0
    
    def hasNext: Boolean = position < items.length
    
    def next(): T = {
        val result = items(position)
        position += 1
        result
    }
}

class ArrayCollection[T](items: Vector[T]) extends CustomCollection[T] {
    def createIterator(): CustomIterator[T] = new ArrayIterator(items)
}

object Main extends App {
    val collection = new ArrayCollection(Vector(10, 20, 30))
    val it = collection.createIterator()
    
    while (it.hasNext) {
        print(it.next() + " ")
    }
    println()
}
```

<!-- REGISTRY_PATH: iterator.languages.typescript -->
### typescript

```typescript
interface IIterator {
    hasNext(): boolean;
    next(): number;
}

interface ICollection {
    createIterator(): IIterator;
}

class ArrayIterator implements IIterator {
    private position = 0;
    
    constructor(private items: number[]) {}
    
    hasNext(): boolean {
        return this.position < this.items.length;
    }
    
    next(): number {
        return this.items[this.position++];
    }
}

class ArrayCollection implements ICollection {
    private items: number[] = [];
    
    add(item: number): void {
        this.items.push(item);
    }
    
    createIterator(): IIterator {
        return new ArrayIterator(this.items);
    }
}

const collection = new ArrayCollection();
collection.add(10);
collection.add(20);
collection.add(30);

const it = collection.createIterator();
let result = "";
while (it.hasNext()) {
    result += it.next() + " ";
}
console.log(result);
```

## mediator

- Docs: /legacy_content/docs/design_pattern/mediator/README.md

<!-- REGISTRY_PATH: mediator.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>

class Mediator {
public:
    virtual ~Mediator() = default;
    virtual void notify(void* sender, const std::string& event) = 0;
};

class User {
protected:
    std::shared_ptr<Mediator> mediator;
    std::string name;
public:
    User(std::shared_ptr<Mediator> m, const std::string& n) : mediator(m), name(n) {}
    virtual ~User() = default;
    virtual void send(const std::string& msg) = 0;
    virtual void receive(const std::string& msg) = 0;
};

class ChatUser : public User {
public:
    using User::User;
    
    void send(const std::string& msg) override {
        std::cout << name << " sends: " << msg << std::endl;
        mediator->notify(this, msg);
    }
    
    void receive(const std::string& msg) override {
        std::cout << name << " receives: " << msg << std::endl;
    }
};

class ChatRoom : public Mediator {
private:
    std::shared_ptr<ChatUser> user1, user2;
public:
    void addUser(std::shared_ptr<ChatUser> u1, std::shared_ptr<ChatUser> u2) {
        user1 = u1;
        user2 = u2;
    }
    
    void notify(void* sender, const std::string& event) override {
        if (sender == user1.get()) {
            user2->receive(event);
        } else {
            user1->receive(event);
        }
    }
};

int main() {
    auto room = std::make_shared<ChatRoom>();
    auto u1 = std::make_shared<ChatUser>(room, "Alice");
    auto u2 = std::make_shared<ChatUser>(room, "Bob");
    
    room->addUser(u1, u2);
    
    u1->send("Hello!");
    u2->send("Hi there!");
}
```

<!-- REGISTRY_PATH: mediator.languages.go -->
### go

```go
package main

import "fmt"

type Mediator interface {
	Notify(sender interface{}, event string)
}

type User struct {
	mediator Mediator
	name     string
}

func (u *User) Send(msg string) {
	fmt.Printf("%s sends: %s\n", u.name, msg)
	u.mediator.Notify(u, msg)
}

func (u *User) Receive(msg string) {
	fmt.Printf("%s receives: %s\n", u.name, msg)
}

type ChatRoom struct {
	user1 *User
	user2 *User
}

func (cr *ChatRoom) AddUsers(u1, u2 *User) {
	cr.user1 = u1
	cr.user2 = u2
}

func (cr *ChatRoom) Notify(sender interface{}, event string) {
	if sender == cr.user1 {
		cr.user2.Receive(event)
	} else {
		cr.user1.Receive(event)
	}
}

func main() {
	room := &ChatRoom{}
	u1 := &User{room, "Alice"}
	u2 := &User{room, "Bob"}

	room.AddUsers(u1, u2)

	u1.Send("Hello!")
	u2.Send("Hi there!")
}
```

<!-- REGISTRY_PATH: mediator.languages.python -->
### python

```python
from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: "User", event: str) -> None:
        pass

class User:
    def __init__(self, mediator: Mediator, name: str):
        self.mediator = mediator
        self.name = name
    
    def send(self, msg: str) -> None:
        print(f"{self.name} sends: {msg}")
        self.mediator.notify(self, msg)
    
    def receive(self, msg: str) -> None:
        print(f"{self.name} receives: {msg}")

class ChatRoom(Mediator):
    def __init__(self):
        self.user1: User = None
        self.user2: User = None
    
    def add_users(self, u1: User, u2: User) -> None:
        self.user1 = u1
        self.user2 = u2
    
    def notify(self, sender: User, event: str) -> None:
        if sender == self.user1:
            self.user2.receive(event)
        else:
            self.user1.receive(event)

room = ChatRoom()
u1 = User(room, "Alice")
u2 = User(room, "Bob")

room.add_users(u1, u2)

u1.send("Hello!")
u2.send("Hi there!")
```

<!-- REGISTRY_PATH: mediator.languages.scala -->
### scala

```scala
// Mediator
trait ChatMediator {
    def sendMessage(sender: ChatUser, msg: String): Unit
}

class ChatRoom extends ChatMediator {
    private var user1: Option[ChatUser] = None
    private var user2: Option[ChatUser] = None
    
    def addUsers(u1: ChatUser, u2: ChatUser): Unit = {
        user1 = Some(u1)
        user2 = Some(u2)
    }
    
    def sendMessage(sender: ChatUser, msg: String): Unit = {
        if (sender == user1.orNull) {
            user2.foreach(_.receive(msg))
        } else {
            user1.foreach(_.receive(msg))
        }
    }
}

class ChatUser(name: String, mediator: ChatMediator) {
    def send(msg: String): Unit = {
        println(s"$name sends: $msg")
        mediator.sendMessage(this, msg)
    }
    
    def receive(msg: String): Unit = {
        println(s"$name receives: $msg")
    }
}

object Main extends App {
    val room = new ChatRoom()
    val u1 = new ChatUser("Alice", room)
    val u2 = new ChatUser("Bob", room)
    
    room.addUsers(u1, u2)
    
    u1.send("Hello!")
    u2.send("Hi there!")
}
```

<!-- REGISTRY_PATH: mediator.languages.typescript -->
### typescript

```typescript
interface IMediator {
    notify(sender: User, event: string): void;
}

class User {
    constructor(protected mediator: IMediator, public name: string) {}
    
    send(msg: string): void {
        console.log(`${this.name} sends: ${msg}`);
        this.mediator.notify(this, msg);
    }
    
    receive(msg: string): void {
        console.log(`${this.name} receives: ${msg}`);
    }
}

class ChatRoom implements IMediator {
    private user1: User;
    private user2: User;
    
    addUsers(u1: User, u2: User): void {
        this.user1 = u1;
        this.user2 = u2;
    }
    
    notify(sender: User, event: string): void {
        if (sender === this.user1) {
            this.user2.receive(event);
        } else {
            this.user1.receive(event);
        }
    }
}

const room = new ChatRoom();
const u1 = new User(room, "Alice");
const u2 = new User(room, "Bob");

room.addUsers(u1, u2);

u1.send("Hello!");
u2.send("Hi there!");
```

## memento

- Docs: /legacy_content/docs/design_pattern/memento/README.md

<!-- REGISTRY_PATH: memento.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>

class Memento {
private:
    std::string state;
public:
    Memento(const std::string& s) : state(s) {}
    std::string getState() const { return state; }
};

class Originator {
private:
    std::string state;
public:
    void setState(const std::string& s) { state = s; }
    std::string getState() const { return state; }
    
    std::shared_ptr<Memento> saveState() {
        return std::make_shared<Memento>(state);
    }
    
    void restoreState(const std::shared_ptr<Memento>& memento) {
        state = memento->getState();
    }
};

class Caretaker {
private:
    std::vector<std::shared_ptr<Memento>> history;
public:
    void save(std::shared_ptr<Memento> memento) {
        history.push_back(memento);
    }
    
    std::shared_ptr<Memento> restore(int index) {
        if (index >= 0 && index < history.size()) {
            return history[index];
        }
        return nullptr;
    }
};

int main() {
    Originator originator;
    Caretaker caretaker;
    
    originator.setState("State 1");
    caretaker.save(originator.saveState());
    
    originator.setState("State 2");
    caretaker.save(originator.saveState());
    
    originator.setState("State 3");
    std::cout << "Current: " << originator.getState() << std::endl;
    
    originator.restoreState(caretaker.restore(0));
    std::cout << "Restored: " << originator.getState() << std::endl;
}
```

<!-- REGISTRY_PATH: memento.languages.go -->
### go

```go
package main

import "fmt"

type Memento struct {
	state string
}

func (m *Memento) GetState() string {
	return m.state
}

type Originator struct {
	state string
}

func (o *Originator) SetState(s string) {
	o.state = s
}

func (o *Originator) GetState() string {
	return o.state
}

func (o *Originator) SaveState() *Memento {
	return &Memento{o.state}
}

func (o *Originator) RestoreState(m *Memento) {
	o.state = m.GetState()
}

type Caretaker struct {
	history []*Memento
}

func (c *Caretaker) Save(m *Memento) {
	c.history = append(c.history, m)
}

func (c *Caretaker) Restore(index int) *Memento {
	if index >= 0 && index < len(c.history) {
		return c.history[index]
	}
	return nil
}

func main() {
	origin := &Originator{}
	caretaker := &Caretaker{}

	origin.SetState("State 1")
	caretaker.Save(origin.SaveState())

	origin.SetState("State 2")
	caretaker.Save(origin.SaveState())

	origin.SetState("State 3")
	fmt.Printf("Current: %s\n", origin.GetState())

	origin.RestoreState(caretaker.Restore(0))
	fmt.Printf("Restored: %s\n", origin.GetState())
}
```

<!-- REGISTRY_PATH: memento.languages.python -->
### python

```python
class Memento:
    def __init__(self, state: str):
        self.state = state
    
    def get_state(self) -> str:
        return self.state

class Originator:
    def __init__(self):
        self.state = ""
    
    def set_state(self, state: str) -> None:
        self.state = state
    
    def get_state(self) -> str:
        return self.state
    
    def save_state(self) -> Memento:
        return Memento(self.state)
    
    def restore_state(self, memento: Memento) -> None:
        self.state = memento.get_state()

class Caretaker:
    def __init__(self):
        self.history: list[Memento] = []
    
    def save(self, memento: Memento) -> None:
        self.history.append(memento)
    
    def restore(self, index: int) -> Memento:
        if 0 <= index < len(self.history):
            return self.history[index]
        return None

originator = Originator()
caretaker = Caretaker()

originator.set_state("State 1")
caretaker.save(originator.save_state())

originator.set_state("State 2")
caretaker.save(originator.save_state())

originator.set_state("State 3")
print(f"Current: {originator.get_state()}")

originator.restore_state(caretaker.restore(0))
print(f"Restored: {originator.get_state()}")
```

<!-- REGISTRY_PATH: memento.languages.scala -->
### scala

```scala
// Memento
case class Memento(state: String)

class Originator(private var state: String) {
    def setState(s: String): Unit = {
        state = s
    }
    
    def getState: String = state
    
    def saveState(): Memento = Memento(state)
    
    def restoreState(memento: Memento): Unit = {
        state = memento.state
    }
}

class Caretaker {
    private var history: List[Memento] = List()
    
    def save(memento: Memento): Unit = {
        history = history :+ memento
    }
    
    def restore(index: Int): Option[Memento] = {
        if (index >= 0 && index < history.length) Some(history(index))
        else None
    }
}

object Main extends App {
    val originator = new Originator("State 1")
    val caretaker = new Caretaker()
    
    caretaker.save(originator.saveState())
    
    originator.setState("State 2")
    caretaker.save(originator.saveState())
    
    originator.setState("State 3")
    println(s"Current: ${originator.getState}")
    
    caretaker.restore(0).foreach(originator.restoreState)
    println(s"Restored: ${originator.getState}")
}
```

<!-- REGISTRY_PATH: memento.languages.typescript -->
### typescript

```typescript
class Memento {
    constructor(private state: string) {}
    
    getState(): string {
        return this.state;
    }
}

class Originator {
    private state: string = "";
    
    setState(state: string): void {
        this.state = state;
    }
    
    getState(): string {
        return this.state;
    }
    
    saveState(): Memento {
        return new Memento(this.state);
    }
    
    restoreState(memento: Memento): void {
        this.state = memento.getState();
    }
}

class Caretaker {
    private history: Memento[] = [];
    
    save(memento: Memento): void {
        this.history.push(memento);
    }
    
    restore(index: number): Memento | null {
        if (index >= 0 && index < this.history.length) {
            return this.history[index];
        }
        return null;
    }
}

const originator = new Originator();
const caretaker = new Caretaker();

originator.setState("State 1");
caretaker.save(originator.saveState());

originator.setState("State 2");
caretaker.save(originator.saveState());

originator.setState("State 3");
console.log(`Current: ${originator.getState()}`);

const restored = caretaker.restore(0);
if (restored) {
    originator.restoreState(restored);
    console.log(`Restored: ${originator.getState()}`);
}
```

## observer

- Docs: /legacy_content/docs/design_pattern/observer/README.md

<!-- REGISTRY_PATH: observer.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <memory>

class Observer {
public:
    virtual ~Observer() = default;
    virtual void update(const std::string& msg) = 0;
};

class Subject {
private:
    std::vector<std::shared_ptr<Observer>> observers;
public:
    void attach(std::shared_ptr<Observer> observer) {
        observers.push_back(observer);
    }
    
    void notify(const std::string& msg) {
        for (auto& obs : observers) {
            obs->update(msg);
        }
    }
};

class ConcreteObserver : public Observer {
private:
    std::string name;
public:
    ConcreteObserver(const std::string& n) : name(n) {}
    
    void update(const std::string& msg) override {
        std::cout << name << " received: " << msg << std::endl;
    }
};

int main() {
    auto subject = std::make_shared<Subject>();
    auto obs1 = std::make_shared<ConcreteObserver>("Observer1");
    auto obs2 = std::make_shared<ConcreteObserver>("Observer2");
    
    subject->attach(obs1);
    subject->attach(obs2);
    
    subject->notify("Event 1");
    subject->notify("Event 2");
}
```

<!-- REGISTRY_PATH: observer.languages.go -->
### go

```go
package main

import "fmt"

type Observer interface {
	Update(msg string)
}

type Subject struct {
	observers []Observer
}

func (s *Subject) Attach(observer Observer) {
	s.observers = append(s.observers, observer)
}

func (s *Subject) Notify(msg string) {
	for _, observer := range s.observers {
		observer.Update(msg)
	}
}

type ConcreteObserver struct {
	name string
}

func (c *ConcreteObserver) Update(msg string) {
	fmt.Printf("%s received: %s\n", c.name, msg)
}

func main() {
	subject := &Subject{}
	obs1 := &ConcreteObserver{"Observer1"}
	obs2 := &ConcreteObserver{"Observer2"}

	subject.Attach(obs1)
	subject.Attach(obs2)

	subject.Notify("Event 1")
	subject.Notify("Event 2")
}
```

<!-- REGISTRY_PATH: observer.languages.python -->
### python

```python
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, msg: str) -> None:
        pass

class Subject:
    def __init__(self):
        self.observers: list[Observer] = []
    
    def attach(self, observer: Observer) -> None:
        self.observers.append(observer)
    
    def notify(self, msg: str) -> None:
        for observer in self.observers:
            observer.update(msg)

class ConcreteObserver(Observer):
    def __init__(self, name: str):
        self.name = name
    
    def update(self, msg: str) -> None:
        print(f"{self.name} received: {msg}")

subject = Subject()
obs1 = ConcreteObserver("Observer1")
obs2 = ConcreteObserver("Observer2")

subject.attach(obs1)
subject.attach(obs2)

subject.notify("Event 1")
subject.notify("Event 2")
```

<!-- REGISTRY_PATH: observer.languages.scala -->
### scala

```scala
// Observer
trait Observer {
    def update(msg: String): Unit
}

class Subject {
    private var observers: List[Observer] = List()
    
    def attach(observer: Observer): Unit = {
        observers = observers :+ observer
    }
    
    def notify(msg: String): Unit = {
        observers.foreach(_.update(msg))
    }
}

class ConcreteObserver(name: String) extends Observer {
    def update(msg: String): Unit = {
        println(s"$name received: $msg")
    }
}

object Main extends App {
    val subject = new Subject()
    val obs1 = new ConcreteObserver("Observer1")
    val obs2 = new ConcreteObserver("Observer2")
    
    subject.attach(obs1)
    subject.attach(obs2)
    
    subject.notify("Event 1")
    subject.notify("Event 2")
}
```

<!-- REGISTRY_PATH: observer.languages.typescript -->
### typescript

```typescript
interface IObserver {
    update(msg: string): void;
}

class Subject {
    private observers: IObserver[] = [];
    
    attach(observer: IObserver): void {
        this.observers.push(observer);
    }
    
    notify(msg: string): void {
        for (const observer of this.observers) {
            observer.update(msg);
        }
    }
}

class ConcreteObserver implements IObserver {
    constructor(private name: string) {}
    
    update(msg: string): void {
        console.log(`${this.name} received: ${msg}`);
    }
}

const subject = new Subject();
const obs1 = new ConcreteObserver("Observer1");
const obs2 = new ConcreteObserver("Observer2");

subject.attach(obs1);
subject.attach(obs2);

subject.notify("Event 1");
subject.notify("Event 2");
```

## prototype

- Docs: /legacy_content/docs/design_pattern/prototype/README.md

<!-- REGISTRY_PATH: prototype.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>
#include <string>

class Shape {
public:
    explicit Shape(std::string color) : color_(std::move(color)) {}
    virtual ~Shape() = default;
    virtual std::unique_ptr<Shape> clone() const = 0;
    virtual void describe() const = 0;

protected:
    std::string color_;
};

class Circle : public Shape {
public:
    Circle(std::string color, int radius) : Shape(std::move(color)), radius_(radius) {}

    std::unique_ptr<Shape> clone() const override {
        return std::make_unique<Circle>(*this);
    }

    void describe() const override {
        std::cout << color_ << " circle radius=" << radius_ << '\n';
    }

private:
    int radius_;
};

int main() {
    Circle templateCircle("blue", 12);
    auto copy = templateCircle.clone();
    templateCircle.describe();
    copy->describe();
}
```

<!-- REGISTRY_PATH: prototype.languages.go -->
### go

```go
package main

import "fmt"

type Prototype interface {
	Clone() Prototype
	Describe()
}

type Report struct {
	Title string
	Tags  []string
}

func (r Report) Clone() Prototype {
	tags := append([]string(nil), r.Tags...)
	return Report{Title: r.Title, Tags: tags}
}

func (r Report) Describe() {
	fmt.Printf("%s %v\n", r.Title, r.Tags)
}

func main() {
	template := Report{Title: "weekly", Tags: []string{"ops", "summary"}}
	copy := template.Clone()
	template.Describe()
	copy.Describe()
}
```

<!-- REGISTRY_PATH: prototype.languages.python -->
### python

```python
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Report:
    title: str
    tags: list[str]

    def clone(self) -> "Report":
        return deepcopy(self)


template = Report("weekly", ["ops", "summary"])
copy = template.clone()

print(template)
print(copy)
```

<!-- REGISTRY_PATH: prototype.languages.scala -->
### scala

```scala
// Prototype
trait Prototype {
    def clone(): Prototype
}

case class Document(title: String, content: String) extends Prototype {
    def clone(): Document = this.copy()
}

object Main extends App {
    val original = Document("Report", "Initial content")
    val copy1 = original.clone()
    val copy2 = original.clone()
    
    println(original)
    println(copy1)
    println(copy2)
}
```

<!-- REGISTRY_PATH: prototype.languages.typescript -->
### typescript

```typescript
interface Prototype<T> {
  clone(): T;
}

class Report implements Prototype<Report> {
  constructor(
    public readonly title: string,
    public readonly tags: string[],
  ) {}

  clone(): Report {
    return new Report(this.title, [...this.tags]);
  }
}

const template = new Report('weekly', ['ops', 'summary']);
const copy = template.clone();

console.log(template);
console.log(copy);
```

## proxy

- Docs: /legacy_content/docs/design_pattern/proxy/README.md

<!-- REGISTRY_PATH: proxy.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>

struct Image {
    virtual ~Image() = default;
    virtual void display() = 0;
};

class RealImage : public Image {
public:
    RealImage() {
        std::cout << "load image\n";
    }

    void display() override {
        std::cout << "display image\n";
    }
};

class ImageProxy : public Image {
public:
    void display() override {
        if (!real_) {
            real_ = std::make_unique<RealImage>();
        }
        real_->display();
    }

private:
    std::unique_ptr<RealImage> real_;
};

int main() {
    ImageProxy proxy;
    proxy.display();
    proxy.display();
}
```

<!-- REGISTRY_PATH: proxy.languages.go -->
### go

```go
package main

import "fmt"

type Image interface {
	Display()
}

type RealImage struct{}

func NewRealImage() *RealImage {
	fmt.Println("load image")
	return &RealImage{}
}

func (RealImage) Display() {
	fmt.Println("display image")
}

type ImageProxy struct {
	real *RealImage
}

func (p *ImageProxy) Display() {
	if p.real == nil {
		p.real = NewRealImage()
	}
	p.real.Display()
}

func main() {
	proxy := &ImageProxy{}
	proxy.Display()
	proxy.Display()
}
```

<!-- REGISTRY_PATH: proxy.languages.python -->
### python

```python
class RealImage:
    def __init__(self) -> None:
        print("load image")

    def display(self) -> None:
        print("display image")


class ImageProxy:
    def __init__(self) -> None:
        self._real: RealImage | None = None

    def display(self) -> None:
        if self._real is None:
            self._real = RealImage()
        self._real.display()


proxy = ImageProxy()
proxy.display()
proxy.display()
```

<!-- REGISTRY_PATH: proxy.languages.scala -->
### scala

```scala
// Proxy
trait Image {
    def display(): Unit
}

class RealImage(filename: String) extends Image {
    private def loadFromDisk(): Unit = println(s"Loading $filename from disk")
    
    def display(): Unit = {
        loadFromDisk()
        println(s"Displaying $filename")
    }
}

class ImageProxy(filename: String) extends Image {
    private var realImage: Option[RealImage] = None
    
    def display(): Unit = {
        if (realImage.isEmpty) {
            realImage = Some(new RealImage(filename))
        }
        realImage.get.display()
    }
}

object Main extends App {
    val image: Image = new ImageProxy("photo.jpg")
    image.display()
    image.display()
}
```

<!-- REGISTRY_PATH: proxy.languages.typescript -->
### typescript

```typescript
class RealImage {
  constructor() {
    console.log('load image');
  }

  display(): void {
    console.log('display image');
  }
}

class ImageProxy {
  private real: RealImage | null = null;

  display(): void {
    if (!this.real) {
      this.real = new RealImage();
    }
    this.real.display();
  }
}

const proxy = new ImageProxy();
proxy.display();
proxy.display();
```

## singleton

- Docs: /legacy_content/docs/design_pattern/singleton/README.md

<!-- REGISTRY_PATH: singleton.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>

class Config {
public:
    static Config& instance() {
        static Config config;
        return config;
    }

    void setEnv(std::string value) {
        env_ = std::move(value);
    }

    const std::string& env() const {
        return env_;
    }

private:
    Config() = default;
    std::string env_ = "dev";
};

int main() {
    Config::instance().setEnv("prod");
    std::cout << Config::instance().env() << '\n';
}
```

<!-- REGISTRY_PATH: singleton.languages.go -->
### go

```go
package main

import (
	"fmt"
	"sync"
)

type Config struct {
	Env string
}

var (
	once   sync.Once
	shared *Config
)

func Instance() *Config {
	once.Do(func() {
		shared = &Config{Env: "dev"}
	})
	return shared
}

func main() {
	Instance().Env = "prod"
	fmt.Println(Instance().Env)
}
```

<!-- REGISTRY_PATH: singleton.languages.python -->
### python

```python
class Config:
    _instance: "Config | None" = None

    def __new__(cls) -> "Config":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.env = "dev"
        return cls._instance


Config().env = "prod"
print(Config().env)
```

<!-- REGISTRY_PATH: singleton.languages.scala -->
### scala

```scala
// Singleton
object Config {
    private var env: String = "dev"

    def getEnv(): String = env
    
    def setEnv(e: String): Unit = {
        env = e
    }
}

object Main extends App {
    println(Config.getEnv())
    Config.setEnv("prod")
    println(Config.getEnv())
}
```

<!-- REGISTRY_PATH: singleton.languages.typescript -->
### typescript

```typescript
class Config {
  private static shared: Config | null = null;

  private constructor(public env: string) {}

  static instance(): Config {
    if (!Config.shared) {
      Config.shared = new Config('dev');
    }
    return Config.shared;
  }
}

Config.instance().env = 'prod';
console.log(Config.instance().env);
```

## state

- Docs: /legacy_content/docs/design_pattern/state/README.md

<!-- REGISTRY_PATH: state.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>

class State {
public:
    virtual ~State() = default;
    virtual void handle() = 0;
};

class StartState : public State {
public:
    void handle() override {
        std::cout << "Entering start state\n";
    }
};

class RunningState : public State {
public:
    void handle() override {
        std::cout << "Running state active\n";
    }
};

class StoppedState : public State {
public:
    void handle() override {
        std::cout << "Stopped state active\n";
    }
};

class Context {
private:
    std::shared_ptr<State> state;
public:
    void setState(std::shared_ptr<State> s) { state = s; }
    void request() { state->handle(); }
};

int main() {
    Context ctx;
    
    ctx.setState(std::make_shared<StartState>());
    ctx.request();
    
    ctx.setState(std::make_shared<RunningState>());
    ctx.request();
    
    ctx.setState(std::make_shared<StoppedState>());
    ctx.request();
}
```

<!-- REGISTRY_PATH: state.languages.go -->
### go

```go
package main

import "fmt"

type State interface {
	Handle()
}

type StartState struct{}

func (s *StartState) Handle() {
	fmt.Println("Entering start state")
}

type RunningState struct{}

func (s *RunningState) Handle() {
	fmt.Println("Running state active")
}

type StoppedState struct{}

func (s *StoppedState) Handle() {
	fmt.Println("Stopped state active")
}

type Context struct {
	state State
}

func (c *Context) SetState(s State) {
	c.state = s
}

func (c *Context) Request() {
	c.state.Handle()
}

func main() {
	ctx := &Context{}

	ctx.SetState(&StartState{})
	ctx.Request()

	ctx.SetState(&RunningState{})
	ctx.Request()

	ctx.SetState(&StoppedState{})
	ctx.Request()
}
```

<!-- REGISTRY_PATH: state.languages.python -->
### python

```python
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self) -> None:
        pass

class StartState(State):
    def handle(self) -> None:
        print("Entering start state")

class RunningState(State):
    def handle(self) -> None:
        print("Running state active")

class StoppedState(State):
    def handle(self) -> None:
        print("Stopped state active")

class Context:
    def __init__(self):
        self.state: State = None
    
    def set_state(self, state: State) -> None:
        self.state = state
    
    def request(self) -> None:
        self.state.handle()

ctx = Context()

ctx.set_state(StartState())
ctx.request()

ctx.set_state(RunningState())
ctx.request()

ctx.set_state(StoppedState())
ctx.request()
```

<!-- REGISTRY_PATH: state.languages.scala -->
### scala

```scala
// State
trait State {
    def handle(): Unit
}

class StartState extends State {
    def handle(): Unit = println("Entering start state")
}

class RunningState extends State {
    def handle(): Unit = println("Running state active")
}

class StoppedState extends State {
    def handle(): Unit = println("Stopped state active")
}

class Context(private var state: State) {
    def setState(s: State): Unit = {
        state = s
    }
    
    def request(): Unit = {
        state.handle()
    }
}

object Main extends App {
    val ctx = new Context(new StartState())
    
    ctx.request()
    
    ctx.setState(new RunningState())
    ctx.request()
    
    ctx.setState(new StoppedState())
    ctx.request()
}
```

<!-- REGISTRY_PATH: state.languages.typescript -->
### typescript

```typescript
interface IState {
    handle(): void;
}

class StartState implements IState {
    handle(): void {
        console.log("Entering start state");
    }
}

class RunningState implements IState {
    handle(): void {
        console.log("Running state active");
    }
}

class StoppedState implements IState {
    handle(): void {
        console.log("Stopped state active");
    }
}

class Context {
    private state: IState;
    
    setState(state: IState): void {
        this.state = state;
    }
    
    request(): void {
        this.state.handle();
    }
}

const ctx = new Context();

ctx.setState(new StartState());
ctx.request();

ctx.setState(new RunningState());
ctx.request();

ctx.setState(new StoppedState());
ctx.request();
```

## strategy

- Docs: /legacy_content/docs/design_pattern/strategy/README.md

<!-- REGISTRY_PATH: strategy.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>

class Strategy {
public:
    virtual ~Strategy() = default;
    virtual int execute(int a, int b) = 0;
};

class AddStrategy : public Strategy {
public:
    int execute(int a, int b) override {
        return a + b;
    }
};

class SubtractStrategy : public Strategy {
public:
    int execute(int a, int b) override {
        return a - b;
    }
};

class MultiplyStrategy : public Strategy {
public:
    int execute(int a, int b) override {
        return a * b;
    }
};

class Context {
private:
    std::shared_ptr<Strategy> strategy;
public:
    void setStrategy(std::shared_ptr<Strategy> s) { strategy = s; }
    int executeStrategy(int a, int b) { return strategy->execute(a, b); }
};

int main() {
    Context ctx;
    
    ctx.setStrategy(std::make_shared<AddStrategy>());
    std::cout << "Add: " << ctx.executeStrategy(5, 3) << std::endl;
    
    ctx.setStrategy(std::make_shared<SubtractStrategy>());
    std::cout << "Subtract: " << ctx.executeStrategy(5, 3) << std::endl;
    
    ctx.setStrategy(std::make_shared<MultiplyStrategy>());
    std::cout << "Multiply: " << ctx.executeStrategy(5, 3) << std::endl;
}
```

<!-- REGISTRY_PATH: strategy.languages.go -->
### go

```go
package main

import "fmt"

type Strategy interface {
	Execute(int, int) int
}

type AddStrategy struct{}

func (s *AddStrategy) Execute(a, b int) int {
	return a + b
}

type SubtractStrategy struct{}

func (s *SubtractStrategy) Execute(a, b int) int {
	return a - b
}

type MultiplyStrategy struct{}

func (s *MultiplyStrategy) Execute(a, b int) int {
	return a * b
}

type Context struct {
	strategy Strategy
}

func (c *Context) SetStrategy(s Strategy) {
	c.strategy = s
}

func (c *Context) ExecuteStrategy(a, b int) int {
	return c.strategy.Execute(a, b)
}

func main() {
	ctx := &Context{}

	ctx.SetStrategy(&AddStrategy{})
	fmt.Printf("Add: %d\n", ctx.ExecuteStrategy(5, 3))

	ctx.SetStrategy(&SubtractStrategy{})
	fmt.Printf("Subtract: %d\n", ctx.ExecuteStrategy(5, 3))

	ctx.SetStrategy(&MultiplyStrategy{})
	fmt.Printf("Multiply: %d\n", ctx.ExecuteStrategy(5, 3))
}
```

<!-- REGISTRY_PATH: strategy.languages.python -->
### python

```python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> int:
        pass

class AddStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a + b

class SubtractStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a - b

class MultiplyStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a * b

class Context:
    def __init__(self):
        self.strategy: Strategy = None
    
    def set_strategy(self, strategy: Strategy) -> None:
        self.strategy = strategy
    
    def execute_strategy(self, a: int, b: int) -> int:
        return self.strategy.execute(a, b)

ctx = Context()

ctx.set_strategy(AddStrategy())
print(f"Add: {ctx.execute_strategy(5, 3)}")

ctx.set_strategy(SubtractStrategy())
print(f"Subtract: {ctx.execute_strategy(5, 3)}")

ctx.set_strategy(MultiplyStrategy())
print(f"Multiply: {ctx.execute_strategy(5, 3)}")
```

<!-- REGISTRY_PATH: strategy.languages.scala -->
### scala

```scala
// Strategy
trait Strategy {
    def execute(a: Int, b: Int): Int
}

class AddStrategy extends Strategy {
    def execute(a: Int, b: Int): Int = a + b
}

class SubtractStrategy extends Strategy {
    def execute(a: Int, b: Int): Int = a - b
}

class MultiplyStrategy extends Strategy {
    def execute(a: Int, b: Int): Int = a * b
}

class Context(private var strategy: Strategy) {
    def setStrategy(s: Strategy): Unit = {
        strategy = s
    }
    
    def executeStrategy(a: Int, b: Int): Int = {
        strategy.execute(a, b)
    }
}

object Main extends App {
    val ctx = new Context(new AddStrategy())
    
    println(s"Add: ${ctx.executeStrategy(5, 3)}")
    
    ctx.setStrategy(new SubtractStrategy())
    println(s"Subtract: ${ctx.executeStrategy(5, 3)}")
    
    ctx.setStrategy(new MultiplyStrategy())
    println(s"Multiply: ${ctx.executeStrategy(5, 3)}")
}
```

<!-- REGISTRY_PATH: strategy.languages.typescript -->
### typescript

```typescript
interface IStrategy {
    execute(a: number, b: number): number;
}

class AddStrategy implements IStrategy {
    execute(a: number, b: number): number {
        return a + b;
    }
}

class SubtractStrategy implements IStrategy {
    execute(a: number, b: number): number {
        return a - b;
    }
}

class MultiplyStrategy implements IStrategy {
    execute(a: number, b: number): number {
        return a * b;
    }
}

class Context {
    private strategy: IStrategy;
    
    setStrategy(strategy: IStrategy): void {
        this.strategy = strategy;
    }
    
    executeStrategy(a: number, b: number): number {
        return this.strategy.execute(a, b);
    }
}

const ctx = new Context();

ctx.setStrategy(new AddStrategy());
console.log(`Add: ${ctx.executeStrategy(5, 3)}`);

ctx.setStrategy(new SubtractStrategy());
console.log(`Subtract: ${ctx.executeStrategy(5, 3)}`);

ctx.setStrategy(new MultiplyStrategy());
console.log(`Multiply: ${ctx.executeStrategy(5, 3)}`);
```

## template_method

- Docs: /legacy_content/docs/design_pattern/template_method/README.md

<!-- REGISTRY_PATH: template_method.languages.cpp -->
### cpp

```cpp
#include <iostream>

class DataProcessor {
public:
    virtual ~DataProcessor() = default;
    
    void process() {
        readData();
        parseData();
        writeData();
    }
    
protected:
    virtual void readData() = 0;
    virtual void parseData() = 0;
    virtual void writeData() = 0;
};

class CSVProcessor : public DataProcessor {
protected:
    void readData() override {
        std::cout << "Reading CSV data\n";
    }
    
    void parseData() override {
        std::cout << "Parsing CSV\n";
    }
    
    void writeData() override {
        std::cout << "Writing processed CSV\n";
    }
};

class JSONProcessor : public DataProcessor {
protected:
    void readData() override {
        std::cout << "Reading JSON data\n";
    }
    
    void parseData() override {
        std::cout << "Parsing JSON\n";
    }
    
    void writeData() override {
        std::cout << "Writing processed JSON\n";
    }
};

int main() {
    CSVProcessor csv;
    csv.process();
    
    JSONProcessor json;
    json.process();
}
```

<!-- REGISTRY_PATH: template_method.languages.go -->
### go

```go
package main

import "fmt"

type DataProcessor interface {
	ReadData()
	ParseData()
	WriteData()
	Process()
}

type BaseProcessor struct {
	processor DataProcessor
}

func (b *BaseProcessor) Process() {
	b.processor.ReadData()
	b.processor.ParseData()
	b.processor.WriteData()
}

type CSVProcessor struct {
	BaseProcessor
}

func (c *CSVProcessor) ReadData() {
	fmt.Println("Reading CSV data")
}

func (c *CSVProcessor) ParseData() {
	fmt.Println("Parsing CSV")
}

func (c *CSVProcessor) WriteData() {
	fmt.Println("Writing processed CSV")
}

type JSONProcessor struct {
	BaseProcessor
}

func (j *JSONProcessor) ReadData() {
	fmt.Println("Reading JSON data")
}

func (j *JSONProcessor) ParseData() {
	fmt.Println("Parsing JSON")
}

func (j *JSONProcessor) WriteData() {
	fmt.Println("Writing processed JSON")
}

func main() {
	csv := &CSVProcessor{}
	csv.processor = csv
	csv.Process()

	json := &JSONProcessor{}
	json.processor = json
	json.Process()
}
```

<!-- REGISTRY_PATH: template_method.languages.python -->
### python

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process(self) -> None:
        self.read_data()
        self.parse_data()
        self.write_data()
    
    @abstractmethod
    def read_data(self) -> None:
        pass
    
    @abstractmethod
    def parse_data(self) -> None:
        pass
    
    @abstractmethod
    def write_data(self) -> None:
        pass

class CSVProcessor(DataProcessor):
    def read_data(self) -> None:
        print("Reading CSV data")
    
    def parse_data(self) -> None:
        print("Parsing CSV")
    
    def write_data(self) -> None:
        print("Writing processed CSV")

class JSONProcessor(DataProcessor):
    def read_data(self) -> None:
        print("Reading JSON data")
    
    def parse_data(self) -> None:
        print("Parsing JSON")
    
    def write_data(self) -> None:
        print("Writing processed JSON")

csv = CSVProcessor()
csv.process()

json = JSONProcessor()
json.process()
```

<!-- REGISTRY_PATH: template_method.languages.scala -->
### scala

```scala
// Template Method
abstract class DataProcessor {
    final def process(): Unit = {
        readData()
        parseData()
        writeData()
    }
    
    protected def readData(): Unit
    protected def parseData(): Unit
    protected def writeData(): Unit
}

class CSVProcessor extends DataProcessor {
    protected def readData(): Unit = println("Reading CSV data")
    protected def parseData(): Unit = println("Parsing CSV")
    protected def writeData(): Unit = println("Writing processed CSV")
}

class JSONProcessor extends DataProcessor {
    protected def readData(): Unit = println("Reading JSON data")
    protected def parseData(): Unit = println("Parsing JSON")
    protected def writeData(): Unit = println("Writing processed JSON")
}

object Main extends App {
    val csv: DataProcessor = new CSVProcessor()
    csv.process()
    
    println()
    
    val json: DataProcessor = new JSONProcessor()
    json.process()
}
```

<!-- REGISTRY_PATH: template_method.languages.typescript -->
### typescript

```typescript
abstract class DataProcessor {
    process(): void {
        this.readData();
        this.parseData();
        this.writeData();
    }
    
    protected abstract readData(): void;
    protected abstract parseData(): void;
    protected abstract writeData(): void;
}

class CSVProcessor extends DataProcessor {
    protected readData(): void {
        console.log("Reading CSV data");
    }
    
    protected parseData(): void {
        console.log("Parsing CSV");
    }
    
    protected writeData(): void {
        console.log("Writing processed CSV");
    }
}

class JSONProcessor extends DataProcessor {
    protected readData(): void {
        console.log("Reading JSON data");
    }
    
    protected parseData(): void {
        console.log("Parsing JSON");
    }
    
    protected writeData(): void {
        console.log("Writing processed JSON");
    }
}

const csv = new CSVProcessor();
csv.process();

const json = new JSONProcessor();
json.process();
```

## visitor

- Docs: /legacy_content/docs/design_pattern/visitor/README.md

<!-- REGISTRY_PATH: visitor.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>

class Visitor;

class Element {
public:
    virtual ~Element() = default;
    virtual void accept(Visitor* visitor) = 0;
};

class Circle : public Element {
public:
    void accept(Visitor* visitor) override;
    void draw() { std::cout << "Drawing circle\n"; }
};

class Rectangle : public Element {
public:
    void accept(Visitor* visitor) override;
    void draw() { std::cout << "Drawing rectangle\n"; }
};

class Visitor {
public:
    virtual ~Visitor() = default;
    virtual void visit(Circle* c) = 0;
    virtual void visit(Rectangle* r) = 0;
};

void Circle::accept(Visitor* visitor) {
    visitor->visit(this);
}

void Rectangle::accept(Visitor* visitor) {
    visitor->visit(this);
}

class DrawVisitor : public Visitor {
public:
    void visit(Circle* c) override {
        c->draw();
    }
    
    void visit(Rectangle* r) override {
        r->draw();
    }
};

int main() {
    auto circle = std::make_shared<Circle>();
    auto rectangle = std::make_shared<Rectangle>();
    auto visitor = std::make_shared<DrawVisitor>();
    
    circle->accept(visitor.get());
    rectangle->accept(visitor.get());
}
```

<!-- REGISTRY_PATH: visitor.languages.go -->
### go

```go
package main

import "fmt"

type Visitor interface {
	VisitCircle(*Circle)
	VisitRectangle(*Rectangle)
}

type Element interface {
	Accept(Visitor)
}

type Circle struct{}

func (c *Circle) Accept(v Visitor) {
	v.VisitCircle(c)
}

func (c *Circle) Draw() {
	fmt.Println("Drawing circle")
}

type Rectangle struct{}

func (r *Rectangle) Accept(v Visitor) {
	v.VisitRectangle(r)
}

func (r *Rectangle) Draw() {
	fmt.Println("Drawing rectangle")
}

type DrawVisitor struct{}

func (dv *DrawVisitor) VisitCircle(c *Circle) {
	c.Draw()
}

func (dv *DrawVisitor) VisitRectangle(r *Rectangle) {
	r.Draw()
}

func main() {
	circle := &Circle{}
	rectangle := &Rectangle{}
	visitor := &DrawVisitor{}

	circle.Accept(visitor)
	rectangle.Accept(visitor)
}
```

<!-- REGISTRY_PATH: visitor.languages.python -->
### python

```python
from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: "Circle") -> None:
        pass
    
    @abstractmethod
    def visit_rectangle(self, rectangle: "Rectangle") -> None:
        pass

class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

class Circle(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_circle(self)
    
    def draw(self) -> None:
        print("Drawing circle")

class Rectangle(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_rectangle(self)
    
    def draw(self) -> None:
        print("Drawing rectangle")

class DrawVisitor(Visitor):
    def visit_circle(self, circle: Circle) -> None:
        circle.draw()
    
    def visit_rectangle(self, rectangle: Rectangle) -> None:
        rectangle.draw()

circle = Circle()
rectangle = Rectangle()
visitor = DrawVisitor()

circle.accept(visitor)
rectangle.accept(visitor)
```

<!-- REGISTRY_PATH: visitor.languages.scala -->
### scala

```scala
// Visitor
trait Visitor {
    def visitCircle(c: Circle): Unit
    def visitRectangle(r: Rectangle): Unit
}

trait Element {
    def accept(visitor: Visitor): Unit
}

class Circle extends Element {
    def accept(visitor: Visitor): Unit = {
        visitor.visitCircle(this)
    }
    
    def draw(): Unit = println("Drawing circle")
}

class Rectangle extends Element {
    def accept(visitor: Visitor): Unit = {
        visitor.visitRectangle(this)
    }
    
    def draw(): Unit = println("Drawing rectangle")
}

class DrawVisitor extends Visitor {
    def visitCircle(c: Circle): Unit = {
        c.draw()
    }
    
    def visitRectangle(r: Rectangle): Unit = {
        r.draw()
    }
}

object Main extends App {
    val circle = new Circle()
    val rectangle = new Rectangle()
    val visitor = new DrawVisitor()
    
    circle.accept(visitor)
    rectangle.accept(visitor)
}
```

<!-- REGISTRY_PATH: visitor.languages.typescript -->
### typescript

```typescript
interface IVisitor {
    visitCircle(c: Circle): void;
    visitRectangle(r: Rectangle): void;
}

interface IElement {
    accept(visitor: IVisitor): void;
}

class Circle implements IElement {
    accept(visitor: IVisitor): void {
        visitor.visitCircle(this);
    }
    
    draw(): void {
        console.log("Drawing circle");
    }
}

class Rectangle implements IElement {
    accept(visitor: IVisitor): void {
        visitor.visitRectangle(this);
    }
    
    draw(): void {
        console.log("Drawing rectangle");
    }
}

class DrawVisitor implements IVisitor {
    visitCircle(c: Circle): void {
        c.draw();
    }
    
    visitRectangle(r: Rectangle): void {
        r.draw();
    }
}

const circle = new Circle();
const rectangle = new Rectangle();
const visitor = new DrawVisitor();

circle.accept(visitor);
rectangle.accept(visitor);
```

