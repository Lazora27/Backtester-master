import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
