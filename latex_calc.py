from sympy.parsing.latex import parse_latex
from sympy import Symbol
from colorama import init, Fore, Style
import os

# Initialize colorama
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print(f"{Fore.CYAN}╔════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║    LaTeX Calculator    ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╚════════════════════════╝{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Enter 'q' or 'quit' to exit{Style.RESET_ALL}\n")
        
        # Prompt the user for a LaTeX expression
        latex_expr = input(f"{Fore.GREEN}Please enter a LaTeX expression: {Style.RESET_ALL}")
        
        # Check if user wants to quit
        if latex_expr.lower() in ['q', 'quit']:
            print(f"\n{Fore.CYAN}Goodbye!{Style.RESET_ALL}")
            break
        
        # Parse the LaTeX expression into a Sympy expression
        try:
            expr = parse_latex(latex_expr)
        except Exception as e:
            print(f"{Fore.RED}Error parsing LaTeX:{Style.RESET_ALL}", e)
            input("\nPress Enter to continue...")
            continue

        # Identify free symbols (variables) in the expression
        vars_in_expr = expr.free_symbols
        var_values = {}

        # Ask user for values of any variables
        all_values_valid = True
        for var in vars_in_expr:
            var_name = str(var)
            if var_name not in var_values:
                val = input(f"{Fore.BLUE}Please provide a numeric value for {var_name}: {Style.RESET_ALL}")
                try:
                    val = float(val)
                    var_values[var_name] = val
                except ValueError:
                    print(f"{Fore.RED}Invalid value provided for {var_name}.{Style.RESET_ALL}")
                    input("\nPress Enter to continue...")
                    all_values_valid = False
                    break

        if not all_values_valid:
            continue

        # Substitute and evaluate
        for k, v in var_values.items():
            expr = expr.subs(Symbol(k), v)
        evaluated = expr.evalf()

        # Print the result
        print(f"\n{Fore.GREEN}The evaluated result is: {Fore.WHITE}{evaluated}{Style.RESET_ALL}")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
