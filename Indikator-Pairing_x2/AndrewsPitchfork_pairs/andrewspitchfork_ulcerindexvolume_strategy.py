import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
