import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und Fisher
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'Fisher': 1.0
        })
    )
