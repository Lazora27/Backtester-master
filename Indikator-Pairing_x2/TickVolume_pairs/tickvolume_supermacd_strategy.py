import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und SuperMACD
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'SuperMACD': 1.0
        })
    )
