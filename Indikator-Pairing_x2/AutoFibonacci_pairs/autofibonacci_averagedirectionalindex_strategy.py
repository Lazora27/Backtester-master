import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
