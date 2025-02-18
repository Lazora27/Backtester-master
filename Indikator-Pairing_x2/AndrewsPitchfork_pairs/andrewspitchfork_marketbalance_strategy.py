import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'MarketBalance': 1.0
        })
    )
