import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'AAIISentiment': 1.0
        })
    )
