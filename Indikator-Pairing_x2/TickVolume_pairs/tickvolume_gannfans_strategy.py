import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und GannFans
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'GannFans': 1.0
        })
    )
