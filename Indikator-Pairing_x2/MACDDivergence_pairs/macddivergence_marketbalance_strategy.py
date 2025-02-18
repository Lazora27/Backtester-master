import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MarketBalance
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MarketBalance': 1.0
        })
    )
