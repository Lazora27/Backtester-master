import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
