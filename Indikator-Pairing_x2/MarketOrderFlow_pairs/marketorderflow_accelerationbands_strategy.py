import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'AccelerationBands': 1.0
        })
    )
