import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
