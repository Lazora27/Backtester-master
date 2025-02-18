import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
