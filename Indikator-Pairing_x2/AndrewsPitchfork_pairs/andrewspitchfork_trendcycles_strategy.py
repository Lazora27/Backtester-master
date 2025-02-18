import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und TrendCycles
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'TrendCycles': 1.0
        })
    )
