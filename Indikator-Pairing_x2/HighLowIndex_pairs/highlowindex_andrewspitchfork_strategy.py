import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
