import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'AutoFibonacci': 1.0
        })
    )
