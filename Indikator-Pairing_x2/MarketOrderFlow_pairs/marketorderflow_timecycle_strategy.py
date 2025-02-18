import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'TimeCycle': 1.0
        })
    )
