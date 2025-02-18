import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
