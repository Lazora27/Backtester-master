import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'UlcerIndex': 1.0
        })
    )
