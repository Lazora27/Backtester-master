import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
