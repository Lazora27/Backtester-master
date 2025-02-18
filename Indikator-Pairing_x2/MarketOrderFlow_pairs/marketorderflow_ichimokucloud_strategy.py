import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'IchimokuCloud': 1.0
        })
    )
