import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
