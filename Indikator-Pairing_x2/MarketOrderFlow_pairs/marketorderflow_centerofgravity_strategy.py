import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'CenterOfGravity': 1.0
        })
    )
