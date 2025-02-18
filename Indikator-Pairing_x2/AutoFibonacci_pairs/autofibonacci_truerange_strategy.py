import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und TrueRange
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'TrueRange': 1.0
        })
    )
