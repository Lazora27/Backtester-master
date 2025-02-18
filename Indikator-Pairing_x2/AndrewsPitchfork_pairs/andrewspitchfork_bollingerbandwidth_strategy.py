import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
