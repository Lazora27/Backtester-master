import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und MovingAverage
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'MovingAverage': 1.0
        })
    )
