import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und CycleFinder
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'CycleFinder': 1.0
        })
    )
