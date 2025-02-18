import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
