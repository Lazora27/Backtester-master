import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'AutoFibonacci': 1.0
        })
    )
