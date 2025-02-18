import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'AutoFibonacci': 1.0
        })
    )
