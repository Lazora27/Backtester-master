import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'AccelerationBands': 1.0
        })
    )
