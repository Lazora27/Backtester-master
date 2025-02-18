import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'AverageLogRange': 1.0
        })
    )
