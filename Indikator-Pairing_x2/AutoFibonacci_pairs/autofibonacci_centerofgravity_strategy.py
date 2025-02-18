import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'CenterOfGravity': 1.0
        })
    )
