import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'IchimokuCloud': 1.0
        })
    )
