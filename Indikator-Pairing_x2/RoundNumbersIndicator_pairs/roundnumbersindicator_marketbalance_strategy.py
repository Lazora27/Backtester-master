import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
