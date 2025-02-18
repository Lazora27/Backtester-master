import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
