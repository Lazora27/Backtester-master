import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'AutoFibonacci': 1.0
        })
    )
