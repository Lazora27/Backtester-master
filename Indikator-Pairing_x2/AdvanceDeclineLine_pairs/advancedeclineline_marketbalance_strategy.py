import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'MarketBalance': 1.0
        })
    )
