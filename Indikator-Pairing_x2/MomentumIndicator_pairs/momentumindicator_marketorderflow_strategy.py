import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
