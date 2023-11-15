def PPC_intersection(x1,y1,x2,y2): #solve for the intersection point of ppc
    slope1=y1/x1
    slope2=y2/x2
    if slope1<slope2:
        return [x1,y2]
    else:
        return [x2,y1]

def PPC_chekcpoint(x1,y1,x2,y2,x,y): #check whether a point is on ppc
    point_yintercept = y1 + y2
    point_xintercept = x1 + x2
    slope1 = y1 / x1
    slope2 = y2 / x2
    if slope1 < slope2:
        func1 = lambda x:-slope1 * x + point_yintercept
        func2 = lambda x:-slope2 * x + point_xintercept * slope2
    else:
        func2 = lambda x:-slope1 * x + point_xintercept * slope1
        func1 = lambda x:-slope2 * x + point_yintercept
    if x>point_xintercept or x<0:
        return False
    elif x>PPC_intersection(x1,y1,x2,y2)[0]:
       if func2(x)==y:
           return True
       else:
           return False
    else:
        if func1(x)==y:
            return True
        else:
            return False

def PPC(x1,y1,x2,y2): #input the max amount of two goods each person can produce, output their ppc curve function
    point_yintercept = y1 + y2
    point_xintercept = x1 + x2
    slope1 = y1 / x1
    slope2 = y2 / x2
    intersection=PPC_intersection(x1,y1,x2,y2)
    if slope1 < slope2:
        return f'PPC curve: y={-slope1}x+{point_yintercept} when x<{intersection[0]} and y={-slope2}x+{point_xintercept*slope2} when x>{intersection[0]}. The kink point is {intersection}'
    else:
        return f'PPC curve: y={-slope2}x+{point_yintercept} when x<{intersection[0]} and y={-slope1}x+{point_xintercept*slope1} when x>{intersection[0]}. The kink point is {intersection}'

def PPC_input_x_output_y(x1,y1,x2,y2,n):
    point_yintercept = y1 + y2
    point_xintercept = x1 + x2
    slope1 = y1 / x1
    slope2 = y2 / x2
    if slope1 < slope2:
        func1 = lambda x: -slope1 * x + point_yintercept
        func2 = lambda x: -slope2 * x + point_xintercept * slope2
    else:
        func2 = lambda x: -slope1 * x + point_xintercept * slope1
        func1 = lambda x: -slope2 * x + point_yintercept
    if PPC_intersection(x1,y1,x2,y2)[0]>n:
        return func1(n)
    else:
        return func2(n)
def PPC_ratio(x1,y1,x2,y2,r1,r2): #r1 represents x and r2 represents y
    point_yintercept = y1 + y2
    point_xintercept = x1 + x2
    slope1 = y1 / x1
    slope2 = y2 / x2
    x=0
    intersection_slope = PPC_intersection(x1, y1, x2, y2)[1] / PPC_intersection(x1, y1, x2, y2)[0]
    slope = r2 / r1
    if slope1 < slope2 and slope>intersection_slope:
        x = point_yintercept / (slope + slope1)
    elif slope1 >= slope2 and slope>intersection_slope:
        x = point_yintercept/(slope+slope2)
    elif slope1 < slope2 and slope<=intersection_slope:
        x = point_xintercept * slope2 / (slope + slope2)
    else:
        x=point_xintercept*slope1/(slope+slope1)
    return (x,slope*x)

def PPC_tradewithprice(x1,y1,x2,y2,xprice,yprice): #return the point on PPC where max profit occurs
    point_yintercept = y1 + y2
    point_xintercept = x1 + x2
    a=point_yintercept*yprice
    b=point_xintercept*xprice
    c=PPC_intersection(x1,y1,x2,y2)[0]*xprice+PPC_intersection(x1,y1,x2,y2)[1]*yprice
    max_profit=max(a,b,c)
    if max_profit==a:
        return 0,point_yintercept
    elif max_profit==b:
        return point_xintercept,0
    else:
        return PPC_intersection(x1,y1,x2,y2)[0],PPC_intersection(x1,y1,x2,y2)[1]

def CPC(x1,y1,x2,y2,xprice,yprice): #create a cpc function;
    point_yintercept = y1 + y2
    point_xintercept = x1 + x2
    a = point_yintercept * yprice
    b = point_xintercept * xprice
    c = PPC_intersection(x1, y1, x2, y2)[0] * xprice + PPC_intersection(x1, y1, x2, y2)[1] * yprice
    max_profit = max(a, b, c)
    y_intercept=max_profit/yprice
    x_intercept=max_profit/xprice
    slope=-(y_intercept/x_intercept)
    return f'y={slope}x+{y_intercept}'

def market_demand_curve_aggregation(slope1,constant1,slope2,constant2): #Input two demand functions in form of P(Q); output the aggregated demand functions
    aggregated_slope=1/(1/slope1+1/slope2)
    aggregated_constant=(constant1/slope1+constant2/slope2)/(1/slope1+1/slope2)
    kink_point=[0,0]
    if min(constant2,constant1)==constant1:
        kink_point[0]=(constant1-constant2)/slope2
        kink_point[1]=constant1
        return f'kink point: {kink_point} \n demand curve: P={slope2}Q+{constant2} or Q={1/slope2}P+{-constant2/slope2} when Q<{kink_point[0]} and P>{kink_point[1]} \n demand curve: P={aggregated_slope}Q+{aggregated_constant} or Q={1/aggregated_slope}P+{-aggregated_constant/aggregated_slope} when Q>={kink_point[0]} and P<{kink_point[1]}'
    else:
        kink_point[0] = (constant2 - constant1) / slope1
        kink_point[1] = constant2
        return f'kink point:{kink_point} \n demand curve: P={slope1}Q+{constant1} or Q={1/slope1}P+{-constant1/slope1} when Q<{kink_point[0]} and P>{kink_point[1]} \n demand curve: P={aggregated_slope}Q+{aggregated_constant} or Q={1/aggregated_slope}P+{-aggregated_constant/aggregated_slope} when Q>={kink_point[0]} and P<{kink_point[1]}'


def market_supply_curve_aggregation(slope1,constant1,slope2,constant2): #Input two supply functions in form of P(Q); output the aggregated supply functions
    aggregated_slope = 1 / (1 / slope1 + 1 / slope2)
    aggregated_constant = (constant1 / slope1 + constant2 / slope2) / (1 / slope1 + 1 / slope2)
    kink_point=[0,0]
    if max(constant1,constant2)==constant1:
        kink_point[0]=(constant1-constant2)/slope2
        kink_point[1]=constant1
        return f'kink point: {kink_point} \n supply curve: P={slope2}Q+{constant2} or Q={1 / slope2}P+{-constant2 / slope2} when Q<{kink_point[0]} and P<{kink_point[1]} \n supply curve: P={aggregated_slope}Q+{aggregated_constant} or Q={1 / aggregated_slope}P+{-aggregated_constant / aggregated_slope} when Q>={kink_point[0]} and P>{kink_point[1]}'
    else:
        kink_point[0] = (constant2 - constant1) / slope1
        kink_point[1] = constant2
        return f'kink point: {kink_point} \n supply curve: P={slope1}Q+{constant1} or Q={1 / slope1}P+{-constant1 / slope1} when Q<{kink_point[0]} and P<{kink_point[1]} \n supply curve: P={aggregated_slope}Q+{aggregated_constant} or Q={1 / aggregated_slope}P+{-aggregated_constant / aggregated_slope} when Q>={kink_point[0]} and P>{kink_point[1]}'

def price_elasticity_of_demand_supply_income_two_point(P0,P1,Q0,Q1):
    return ((Q1-Q0)/((Q1+Q0)/2))/((P1-P0)/((P1+P0)/2))

def percent_change_in_price_and_quantity_from_the_shift_of_demand(demand_change, demand_point_elasticity,supply_point_elasticity):
    price_change=demand_change/(supply_point_elasticity+abs(demand_point_elasticity))
    quantity_change=supply_point_elasticity*price_change
    return f'The price change is {price_change}%, and the quantity change is {quantity_change}%'

def percent_change_in_price_and_quantity_from_the_shift_of_supply(supply_change, demand_point_elasticity,supply_point_elasticity):
    price_change = -supply_change / (supply_point_elasticity + abs(demand_point_elasticity))
    quantity_change=demand_point_elasticity*price_change
    return f'The price change is {price_change}%, and the quantity change is {quantity_change}%'

def tax(demand_slope,demand_constant,supply_slope,supply_constant,tax): #in form of Q=slope*P+constant
    old_P=(supply_constant-demand_constant)/(demand_slope-supply_slope)
    old_Q=supply_slope*old_P+supply_constant
    new_Q=(tax+demand_constant/demand_slope-supply_constant/supply_slope)/(1/demand_slope-1/supply_slope)
    new_P=(1/supply_slope)*new_Q-supply_constant/supply_slope
    buyer_price=(new_Q-demand_constant)/demand_slope
    seller_price=(new_Q-supply_constant)/supply_slope
    old_consumer_surplus=(-demand_constant/demand_slope-old_P)*old_Q/2
    old_producer_surplus=(old_P+supply_constant/supply_slope)*old_Q/2
    new_consumer_surplus=new_Q*(-demand_constant/demand_slope-tax-new_P)/2
    new_producer_surplus=new_Q*(new_P+supply_constant/supply_slope)/2
    dead_weight_loss=(old_Q-new_Q)*tax/2
    tax_revenue=new_Q*tax
    buyers_tax_burden = buyer_price-old_P
    seller_tax_burden = old_P-seller_price
    return f' Before tax: \n equilibrium point: {old_Q,old_P} \n consumer surplus: {old_consumer_surplus} \n producer surplus: {old_producer_surplus} \n \n After tax: \n equilibrium point: ({new_Q},{new_P}) \n consumer surplus: {new_consumer_surplus} \n producer surplus: {new_producer_surplus} \n Dwl: {dead_weight_loss} \n tax revenue: {tax_revenue} \n price paid by buyers: {buyer_price} \n price received by sellers: {seller_price} \n buyer tax burden: {buyers_tax_burden} \n seller tax burden: {seller_tax_burden}'


def subsidy(demand_slope,demand_constant,supply_slope,supply_constant,subsidy): #in form of Q=slope*P+constant
    old_P = (supply_constant - demand_constant) / (demand_slope - supply_slope)
    old_Q = supply_slope * old_P + supply_constant
    old_consumer_surplus = (-demand_constant / demand_slope - old_P) * old_Q / 2
    old_producer_surplus = (old_P + supply_constant / supply_slope) * old_Q / 2
    new_Q=(subsidy+supply_constant/supply_slope-demand_constant/demand_slope)/(1/supply_slope-1/demand_slope)
    new_P=(1/supply_slope)*new_Q-supply_constant/supply_slope
    new_consumer_surplus = new_Q * (-demand_constant / demand_slope+subsidy - new_P) / 2
    new_producer_surplus = new_Q * (new_P + supply_constant / supply_slope) / 2
    dead_weight_loss =(new_Q-old_Q)*subsidy/2
    government_subsidy_expenditure=new_Q*subsidy
    buyer_price=(new_Q-demand_constant)/demand_slope
    seller_price = (new_Q - supply_constant) / supply_slope
    buyers_subsidy_benefit=old_P-buyer_price
    seller_subsidy_benefit=seller_price-old_P
    return f' Before subsidy: \n equilibrium point {old_Q, old_P} \n consumer surplus: {old_consumer_surplus} \n producer surplus: {old_producer_surplus}. \n \n After subsidy: \n equilibrium point: {new_Q,new_P} \n consumer surplus: {new_consumer_surplus} \n producer surplus: {new_producer_surplus} \n dwl: {dead_weight_loss} \n government subsidy expenditure: {government_subsidy_expenditure} \n price paid by buyers: {buyer_price} \n price received by sellers: {seller_price} \n buyers subsidy benefit: {buyers_subsidy_benefit} \n seller subsidy benefit: {seller_subsidy_benefit}'

def price_floor(demand_slope,demand_constant,supply_slope,supply_constant,price_floor):
    quantity_transacted = demand_slope * price_floor + demand_constant
    surplus=supply_slope*price_floor+supply_constant-quantity_transacted
    willingness_to_pay=(quantity_transacted-supply_constant)/supply_slope
    consumer_surplus=(-demand_constant/demand_slope-price_floor)*quantity_transacted/2
    highest_producer_surplus=(2*price_floor-willingness_to_pay+supply_constant/supply_slope)*quantity_transacted/2
    quality_waste=quantity_transacted*(price_floor-willingness_to_pay)
    return f' quantity transacted: {quantity_transacted} \n surplus: {surplus} \n willingness to pay at quantity transacted: {willingness_to_pay} \n consumer surplus: {consumer_surplus} \n highest producer surplus: {highest_producer_surplus} \n quality waste: {quality_waste}'

def price_ceiling(demand_slope,demand_constant,supply_slope,supply_constant,price_ceiling):
    quantity_transacted = supply_slope * price_ceiling + supply_constant
    shortage=demand_slope*price_ceiling+demand_constant-quantity_transacted
    willingness_to_pay_at_quantity_transacted=(quantity_transacted-demand_constant)/demand_slope
    lowest_value_consumer_surplus=(-demand_constant/demand_slope-willingness_to_pay_at_quantity_transacted)*quantity_transacted/2
    highest_value_consumer_surplus=(willingness_to_pay_at_quantity_transacted-price_ceiling)*quantity_transacted+(-demand_constant/demand_slope-willingness_to_pay_at_quantity_transacted)*quantity_transacted/2
    bribe=willingness_to_pay_at_quantity_transacted-price_ceiling
    bribe_amount=bribe*quantity_transacted
    wait_in_line=bribe_amount
    producer_surplus=(price_ceiling-(-supply_constant/supply_slope))*quantity_transacted/2
    return f' quantity transacted: {quantity_transacted} \n shortage: {shortage} \n willingness to pay at quantity transacted: {willingness_to_pay_at_quantity_transacted} \n lowest consumer surplus: {lowest_value_consumer_surplus} \n highest consumer surplus: {highest_value_consumer_surplus} \n bribe: {bribe} \n total bribe amount: {bribe_amount} \n wait in line cost: {wait_in_line} \n producer surplus: {producer_surplus}'


def Equilibrium_point_and_economics_surplus_P(demand_slope,demand_constant,supply_slope,supply_constant):
    equailibrium_quantity=(demand_constant-supply_constant)/(supply_slope-demand_slope)
    equailibrium_price=demand_slope*equailibrium_quantity+demand_constant
    cs=(demand_constant-equailibrium_price)*equailibrium_quantity/2
    if supply_constant>=0:
        ps=(equailibrium_price-supply_constant)*equailibrium_quantity/2
        economic_surplus=cs+ps
        return f'the equilibrium point is ({equailibrium_quantity},{equailibrium_price}) with consumer surplus {cs}, producer surplus {ps}, and total economic surplus {economic_surplus}.'
    else:
        return f'the equilibrium point is ({equailibrium_quantity},{equailibrium_price})'

def Equilibrium_point_and_economics_surplus_Q(demand_slope,demand_constant,supply_slope,supply_constant):
    equailibrium_price = (demand_constant - supply_constant) / (supply_slope - demand_slope)
    equailibrium_quantity = demand_constant + demand_slope * equailibrium_price
    cs = (demand_constant / (-demand_slope) - equailibrium_price) * equailibrium_quantity / 2
    if -supply_constant/supply_slope>=0:
        ps=(equailibrium_price-(-supply_constant/supply_slope))*equailibrium_quantity/2
        economic_surplus = cs + ps
    else:
        ps="calculate yourself"
        economic_surplus = "calculate yourself"
    return f'the equilibrium point is ({equailibrium_quantity},{equailibrium_price}) with consumer surplus {cs}, producer surplus {ps}, and total economic surplus {economic_surplus}.'

def deadweight_loss_P(demand_slope,demand_constant,supply_slope,supply_constant,q):
    equailibrium_quantity = (demand_constant - supply_constant) / (supply_slope - demand_slope)
    equailibrium_price = demand_slope * equailibrium_quantity + demand_constant
    p_demand=demand_slope*q+demand_constant
    p_supply=supply_slope*q+supply_constant
    dwl=abs(q-equailibrium_quantity)*abs(p_supply-p_demand)/2
    return dwl

def deadweight_loss_Q(a,c,b,d,q):
    demand_slope=1/a
    demand_constant=-c/a
    supply_slope=1/b
    supply_constant=-d/b
    equailibrium_quantity = (demand_constant - supply_constant) / (supply_slope - demand_slope)
    equailibrium_price = demand_slope * equailibrium_quantity + demand_constant
    p_demand = demand_slope * q + demand_constant
    p_supply = supply_slope * q + supply_constant
    dwl = abs(q - equailibrium_quantity) * abs(p_supply - p_demand) / 2
    return dwl

def Social_efficient_level_with_external_cost(demand_slope,demand_constant,supply_slope,supply_constant,cost):
    MSC_slope = supply_slope
    MSC_constant = supply_constant + cost * (-supply_slope)
    original_price = (demand_constant - supply_constant) / (supply_slope - demand_slope)
    original_quantity = demand_constant + demand_slope * original_price
    original_cs = (demand_constant / (-demand_slope) - original_price) * original_quantity / 2
    if -supply_constant / supply_slope >= 0:
        original_ps = (original_price - (-supply_constant / supply_slope)) * original_quantity / 2
        original_economic_surplus = original_cs + original_ps
    else:
        original_ps = -1
        original_economic_surplus = -1
    social_efficient_price = (demand_constant - MSC_constant) / (MSC_slope - demand_slope)
    social_efficient_quantitity = demand_constant+ demand_slope * social_efficient_price
    new_cs = (demand_constant / (-demand_slope) - social_efficient_price) * social_efficient_quantitity / 2
    if -MSC_constant / MSC_slope >= 0:
        new_ps = (social_efficient_price- (-MSC_constant/ MSC_slope)) * social_efficient_quantitity / 2
        new_economic_surplus = new_cs+new_ps
        dwl=abs(social_efficient_quantitity-original_quantity)*cost/2
    else:
        new_ps = -1
        new_economic_surplus = -1
        dwl = -1
    total_welfare_to_society=new_economic_surplus-dwl
    return f' market equilibrium: \n equilibrium point: ({original_quantity},{original_price}) \n consumer surplus: {original_cs} \n producer surplus: {original_ps} \n economic surplus: {original_economic_surplus} \n DWL to the society: {dwl} \n total welfare to the society: {total_welfare_to_society} \n \n social optimum: \n social efficient point: ({social_efficient_quantitity},{social_efficient_price}) \n consumer surplus {new_cs} \n producer surplus: {new_ps} \n economic surplus: {new_economic_surplus}.'

def Social_efficient_level_with_external_benefit(demand_slope,demand_constant,supply_slope,supply_constant,benefit):
    MSB_slope=demand_slope
    MSB_constant=demand_constant+benefit*(-demand_slope)
    original_price = (demand_constant - supply_constant) / (supply_slope - demand_slope)
    original_quantity = demand_constant + demand_slope * original_price
    original_cs = (demand_constant / (-demand_slope) - original_price) * original_quantity / 2
    if -supply_constant / supply_slope >= 0:
        original_ps = (original_price - (-supply_constant / supply_slope)) * original_quantity / 2
        original_economic_surplus = original_cs + original_ps
    else:
        original_ps=-1
        original_economic_surplus = -1
    social_efficient_price = (MSB_constant - supply_constant) / (supply_slope - MSB_slope)
    social_efficient_quantitity = MSB_constant + MSB_slope * social_efficient_price
    new_cs = (MSB_constant / (-MSB_slope) - social_efficient_price) * social_efficient_quantitity / 2
    if -supply_constant/supply_slope>=0:
        new_ps=(social_efficient_price-(-supply_constant/supply_slope))*social_efficient_quantitity/2
        new_economic_surplus = new_ps+new_cs
        dwl=abs(social_efficient_quantitity-original_quantity)*benefit/2
    else:
        new_ps=-1
        new_economic_surplus = -1
        dwl=-1
    total_welfare_to_society = new_economic_surplus - dwl
    return f' market equilibrium: \n equilibrium point: ({original_quantity},{original_price}) \n consumer surplus: {original_cs} \n producer surplus: {original_ps} \n economic surplus: {original_economic_surplus} \n DWL to the society: {dwl} \n total welfare to the society: {total_welfare_to_society} \n \n social optimum: \n social efficient point: ({social_efficient_quantitity},{social_efficient_price}) \n consumer surplus {new_cs} \n producer surplus: {new_ps} \n economic surplus: {new_economic_surplus}.'

def MSB_efficent_level(demand_slope,demand_constant,supply_slope,supply_constant,MSB_slope,MSB_constant):
    original_price=(demand_constant-supply_constant)/(supply_slope-demand_slope)
    original_quantity=demand_constant+demand_slope*original_price
    original_cs=(demand_constant/(-demand_slope)-original_price)*original_quantity/2
    if -supply_constant/supply_slope>=0:
        original_ps=(original_price-(-supply_constant/supply_slope))*original_quantity/2
        original_economic_surplus = original_cs + original_ps
    else:
        original_ps=-1
        original_economic_surplus = -1
    social_efficient_price=(MSB_constant - supply_constant) / (supply_slope - MSB_slope)
    social_efficient_quantitity= MSB_constant + MSB_slope * social_efficient_price
    new_cs = (MSB_constant / (-MSB_slope) -social_efficient_price) * social_efficient_quantitity / 2
    if -supply_constant/supply_slope>=0:
        new_ps=(social_efficient_price-(-supply_constant/supply_slope))*social_efficient_quantitity/2
        new_economic_surplus = new_ps+new_cs
        dwl=abs(social_efficient_quantitity-original_quantity)*abs(original_price-(original_quantity-MSB_constant)/MSB_slope)/2
    else:
        new_ps=-1
        new_economic_surplus = -1
        dwl=-1
    total_welfare_to_society = new_economic_surplus - dwl
    return f' market equilibrium: \n equilibrium point: ({original_quantity},{original_price}) \n consumer surplus: {original_cs} \n producer surplus: {original_ps} \n economic surplus: {original_economic_surplus} \n DWL to the society: {dwl} \n total welfare to the society: {total_welfare_to_society} \n \n social optimum: \n social efficient point: ({social_efficient_quantitity},{social_efficient_price}) \n consumer surplus {new_cs} \n producer surplus: {new_ps} \n economic surplus: {new_economic_surplus}'

def MSB_aggregation(slope1, constant1, slope2, constant2):
    Q1=-constant1/slope1
    Q2=-constant2/slope2
    if Q1==Q2:
       return f"P={slope1+slope2}Q+{constant1+constant2}"
    elif min(Q1,Q2)==Q1:
        kink_point=[Q1,slope2*Q1+constant2]
        return f" kink point: {kink_point} \n P={slope1+slope2}Q+{constant1+constant2} when Q<{Q1} and P>{kink_point[1]} \n P={slope2}Q+{constant2} otherwise"
    else:
        kink_point=[Q2,slope1*Q2+constant1]
        return f" kink point: {kink_point} \n P={slope1+slope2}Q+{constant1+constant2} when Q<{Q2} and P>{kink_point[1]} \n P={slope1}Q+{constant1} otherwise"

def Perfect_Competition_Model(MC_slope,MC_constant,number_of_firms,demand_slope,demand_constant):
    market_supply_slope=MC_slope/number_of_firms
    market_supply_constant=MC_constant
    market_equailibrium_quantity = (demand_constant - market_supply_constant) / (market_supply_slope - demand_slope)
    market_equailibrium_price = demand_slope * market_equailibrium_quantity + demand_constant
    q=market_equailibrium_quantity/number_of_firms
    return f' market supply curve: P={market_supply_slope}Q+{market_supply_constant} \n short run market equilibrium: ({market_equailibrium_quantity},{market_equailibrium_price}) \n individual firm quantity produced: {q}'

def Price_Discrinmination_without_market_segmentation(slope1,const1,slope2,const2,mc):
    pass

def monopoly_profit_maximaizing(slope_d,constant_d,slope_mc,constant_mc):
    demand_slope=1/slope_d
    demand_constant=-constant_d/slope_d
    slope_mr=2/slope_d
    constant_mr=-constant_d/slope_d
    social_equilibrium_quantity = (demand_constant - constant_mc) / (slope_mc - demand_slope)
    social_equilibrium_price = demand_slope * social_equilibrium_quantity + demand_constant
    Q=(constant_mc-constant_mr)/(slope_mr-slope_mc)
    P=slope_mr/2*Q+constant_mr
    dwl=(P-slope_mc*Q-constant_mc)*(abs(social_equilibrium_quantity-Q))/2
    cs=(demand_constant-P)*Q/2
    ps=(P-constant_mc+P-slope_mc*Q-constant_mc)*Q/2
    return f' monopoly profit maximizing point: ({Q},{P}) \n consumer surplus: {cs} \n monopoly producer surplus: {ps} \n deadweight loss to society: {dwl} \n social optimal point: ({social_equilibrium_quantity},{social_equilibrium_price})'

def monopoly_with_constant_mc_and_price_ceiling(demand_slope,demand_constant,mc,price_ceiling):
    slope_mr=2*demand_slope
    constant_mr=demand_constant
    P=demand_slope*((mc-constant_mr)/slope_mr)+demand_constant
    if price_ceiling>P:
        return 'ineffective price ceiling'
    else:
        Q=(price_ceiling-demand_constant)/demand_slope
        ps=Q*(price_ceiling-mc)
        dwl=(price_ceiling-mc)*((mc-demand_constant)/demand_slope-Q)/2
        return f' equilibrium point({Q},{price_ceiling}) \n monopoly\'s producer surplus: {ps} \n deadweight loss: {dwl}'

def work_separately_total_abcd(a,b,c,d,r1,r2):
    if r1<=r2:
        return b/(r2/r1+b/a)+d/(r2/r1+d/c)
    else:
        return r2/r1*(b/(r2/r1+b/a)+d/(r2/r1+d/c))


print("work separately total abcdxy:")
print(work_separately_total_abcd(60,162,162,60,2,1)) #r1 is x r2 is y
print('')

print("Joint PPC curve:")
print(PPC(22,22/3,26.5,53)) #input the max amount of two goods each person can produce, output their ppc curve function
print('')

print("The maximum amount they can consume for goods y if they consume n goods x:")
print(PPC_input_x_output_y(6,66,25,875,29))  #input the max amount of two goods each person can produce and the amount they want to consume for goods x, input the corresponding amount for goods y
print("")

print("Check whether the point is on the PPC curve:")
print(PPC_chekcpoint(1,1,1,1,1,1)) #check whether a point is on ppc
print('')

print('PPC with ratio:')
print(PPC_ratio(60,162,162,60,2,1)) #r1 represents x and r2 represents y
print('')

print('The point on PPC that maximizes the income')
print(PPC_tradewithprice(100,20,20,100,6,1)) #return the point on PPC where max profit occurs
print('')

print("CPC in an open economy:")
print(CPC(22,22/3,26.5,53,1,2)) #create a cpc function
print('')

print('Market demand curves horizontal aggregation:')
print(market_demand_curve_aggregation(-1/65,1000/65,-1/6.5,100/6.5)) #Input two demand functions in form of P(Q); output the aggregated demand functions
print('')

print('Market supply curves horizontal aggregation:')
print(market_supply_curve_aggregation(0.2,84,0.4,35)) #Input two supply functions in form of P(Q); output the aggregated supply functions
print('')

print('Elasticity two point formula:')
print(price_elasticity_of_demand_supply_income_two_point(11000,9000,20,28)) #Input P0,P1,Q0,Q1
print('')

print("Percent change in price and quantity from the shift of demand:")
print(percent_change_in_price_and_quantity_from_the_shift_of_demand(-3,-0.6,1.79)) #Input demand curve change in percentage, demand point elasticity, and supply point elasticity
print('')

print("Percent change in price and quantity from the shift of supply:")
print(percent_change_in_price_and_quantity_from_the_shift_of_supply(4,-1.7,0.97)) ##Input supply curve change in percentage, demand point elasticity, and supply point elasticity
print('')

print("Tax:")
print(tax(-10,100,20,-50,3)) #in form of Q=slope*P+constant, the last parameter is the tax
print('')

print('Subsidy:')
print(subsidy(-1000,5430,1000,-1120,2)) #in form of Q=slope*P+constant
print('')

print("Price ceiling:")
print(price_ceiling(-1,144,4,-288,81.4)) #input slope and constants in demand and supply curves using Q as subject; the last input is the price ceiling
print('')

print("Price floor:") #input slope and constants in demand and supply curves using Q as subject; the last input is the price floor
print(price_floor(-30,1800,20,-440,49.4))
print('')

print('Social optimum with external cost:')
print(Social_efficient_level_with_external_cost(-0.4,800,0.6,-300,50)) #in form of Q=slope*P+constant
print('')

print('Social optimum with external benefit:')
print(Social_efficient_level_with_external_benefit(-2,510,4,-20,15.1)) #in form of Q=slope*P+constant
print('')

print('Social optimum with given MSB curve:')
print(MSB_efficent_level(-1,200,1.5,-85,-0.9,200)) # in form of Q=slope*P+constant
print('')

print('MSB curves vertical aggregation:')
print(MSB_aggregation(-5.5,100,-4.5,40)) #P as the subject;
print('')

print("Perfect Competition Model:")
print(Perfect_Competition_Model(0.25,20,50,-0.005,1000)) #input mc slope, mc constant, number of firms, demand slope, demand constant
print('')

print('Monopoly Profit Maximizing:')
print(monopoly_profit_maximaizing(-71.5,1100,0,1)) #demand curve Q as subject and then input mc slope mc constant
print('')

print('Monopoly with constant mc and price ceiling:')
print(monopoly_with_constant_mc_and_price_ceiling(-0.5,160,4,5)) #demand curve P as subject and then input mc, price ceiling
print('')

print("Equilibrium point and economic surplus P:")
print(Equilibrium_point_and_economics_surplus_P(-0.5,350,0.6,85)) #in form of P=slope*Q+constant
print('')

print("Equilibrium point and economic surplus Q:")
print(Equilibrium_point_and_economics_surplus_Q(-1,144,4,-288)) #in form of Q=slope*P+constant
print('')

print('Deadweight loss P:')
print(deadweight_loss_P(-0.5,350,0.6,85,300)) #Use P as the subject and input the quantity required
print('')

print('Deadweight loss Q:')
print(deadweight_loss_Q(-0.9,200,1.5,-85,200)) #Use Q as the subject and input the quantity required
print('')
