import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MarketBalance
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MarketBalance': 1.0
        })
    )
