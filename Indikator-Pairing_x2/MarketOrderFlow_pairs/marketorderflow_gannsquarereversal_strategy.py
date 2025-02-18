import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'GannSquareReversal': 1.0
        })
    )
