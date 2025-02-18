import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und VWAPBands
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'VWAPBands': 1.0
        })
    )
