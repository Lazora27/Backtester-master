import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
