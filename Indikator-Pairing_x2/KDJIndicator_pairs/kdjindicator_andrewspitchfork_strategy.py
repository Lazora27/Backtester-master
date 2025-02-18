import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
