import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und BollingerBands
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'BollingerBands': 1.0
        })
    )
