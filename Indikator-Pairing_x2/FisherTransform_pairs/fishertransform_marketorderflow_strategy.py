import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
