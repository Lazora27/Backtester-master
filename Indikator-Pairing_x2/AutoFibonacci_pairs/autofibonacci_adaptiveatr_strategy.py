import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'AdaptiveATR': 1.0
        })
    )
