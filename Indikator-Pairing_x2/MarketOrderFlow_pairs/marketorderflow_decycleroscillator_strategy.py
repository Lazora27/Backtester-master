import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
