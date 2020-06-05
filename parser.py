class Argument:
    # la funzione init accetta come parametri gli argomenti da inserire nel dizionario
    def __init__(self, args=[], particular_args=[]):
        self.accettable_args = args

        # particular_args sta per gli argomenti che non necessitano di altri parametri oltre a se stessi
        self.particular_args = particular_args

        for particular_arg in particular_args:
            if particular_arg not in self.accettable_args:
                self.accettable_args.append(particular_arg)

    def parse(self, args):
        self.arguments = []
        self.parsed_elements = {}

        for arg in args:
            if arg in self.accettable_args:
                self.arguments.append(arg)
                accepted = True
                continue
            elif arg in self.particular_args:
                self.arguments.append(arg)
            else:
                if accepted != True:
                    raise Exception("error")
                    
            if accepted:
                self.arguments.append(arg)
                accepted = False

        while True:
            try:
                try:
                    try:
                        # print(self.arguments)
                        if self.arguments[0] in self.accettable_args:
                            try:
                                if self.arguments[1] in self.accettable_args or self.arguments[1] in self.particular_args:
                                    raise Exception("error")
                            except IndexError:
                                raise Exception("error")

                        if self.arguments[0] in self.accettable_args and self.arguments[1] not in self.particular_args:
                            self.parsed_elements[str(self.arguments.pop())] = self.arguments.pop()
                        elif self.arguments[0] in self.particular_args:
                            self.parsed_elements[str(self.arguments.pop(0))] = True #self.arguments.pop()
                        else:
                            # pass
                            raise Exception("error")
                    except IndexError:
                        try:
                            if self.arguments[0] in self.particular_args:
                                self.parsed_elements[str(self.arguments.pop(0))] = True
                        except IndexError:
                            break
                except AttributeError:
                    # print(self.arguments)
                    if self.arguments[0] in self.accettable_args:
                        self.parsed_elements[str(self.arguments.pop())] = self.arguments.pop()
                    else:
                        raise Exception("error")
            except IndexError:
                break

        # if len(self.parsed_elements)%2!=0:
            # raise Exception("error")
        try:
            for argument in self.particular_args:
                if argument not in self.parsed_elements:
                    self.parsed_elements[argument] = False
        except:
            pass

        return self.parsed_elements

if __name__=="__main__":
    arg = Argument(["-f"], particular_args=["File", "--help"])

    a = arg.parse(["-f", "ciao", "--help", "File", "2"])
    print(a)
