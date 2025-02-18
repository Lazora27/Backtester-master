import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
