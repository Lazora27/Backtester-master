import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'KeltnerChannels': 1.0
        })
    )
