import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'AverageTrueRange': 1.0
        })
    )
