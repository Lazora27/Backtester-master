import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
