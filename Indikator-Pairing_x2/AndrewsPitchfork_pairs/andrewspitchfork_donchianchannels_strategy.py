import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'DonchianChannels': 1.0
        })
    )
