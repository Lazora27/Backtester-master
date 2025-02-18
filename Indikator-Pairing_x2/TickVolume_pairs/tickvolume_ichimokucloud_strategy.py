import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'IchimokuCloud': 1.0
        })
    )
