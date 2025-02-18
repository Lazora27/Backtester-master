import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'AutoFibonacci': 1.0
        })
    )
