import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
