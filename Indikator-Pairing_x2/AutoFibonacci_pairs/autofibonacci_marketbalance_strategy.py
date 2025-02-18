import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'MarketBalance': 1.0
        })
    )
