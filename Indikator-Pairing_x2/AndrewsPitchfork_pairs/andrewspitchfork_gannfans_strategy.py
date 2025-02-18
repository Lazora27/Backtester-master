import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und GannFans
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'GannFans': 1.0
        })
    )
