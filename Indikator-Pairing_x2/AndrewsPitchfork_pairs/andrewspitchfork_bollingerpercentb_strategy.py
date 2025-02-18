import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'BollingerPercentB': 1.0
        })
    )
