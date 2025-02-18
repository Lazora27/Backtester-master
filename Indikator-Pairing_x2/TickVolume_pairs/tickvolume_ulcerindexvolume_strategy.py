import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
