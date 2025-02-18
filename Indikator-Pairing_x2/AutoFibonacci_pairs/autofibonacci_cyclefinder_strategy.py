import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'CycleFinder': 1.0
        })
    )
