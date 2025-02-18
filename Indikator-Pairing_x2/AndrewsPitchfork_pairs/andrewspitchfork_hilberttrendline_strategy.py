import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'HilbertTrendline': 1.0
        })
    )
