import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'WeeklyCycle': 1.0
        })
    )
