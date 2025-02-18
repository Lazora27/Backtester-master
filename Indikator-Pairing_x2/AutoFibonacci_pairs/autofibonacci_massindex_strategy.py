import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und MassIndex
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'MassIndex': 1.0
        })
    )
