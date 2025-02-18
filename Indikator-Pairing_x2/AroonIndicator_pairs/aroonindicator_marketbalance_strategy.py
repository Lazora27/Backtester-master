import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
