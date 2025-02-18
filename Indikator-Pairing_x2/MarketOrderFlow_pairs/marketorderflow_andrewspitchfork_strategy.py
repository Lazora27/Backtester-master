import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
