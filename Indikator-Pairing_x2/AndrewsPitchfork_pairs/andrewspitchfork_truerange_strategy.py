import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und TrueRange
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'TrueRange': 1.0
        })
    )
