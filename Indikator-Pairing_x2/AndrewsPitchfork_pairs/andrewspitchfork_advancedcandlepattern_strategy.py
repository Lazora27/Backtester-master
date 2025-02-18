import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
