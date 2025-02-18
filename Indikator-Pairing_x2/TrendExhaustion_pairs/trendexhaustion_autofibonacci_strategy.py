import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'AutoFibonacci': 1.0
        })
    )
