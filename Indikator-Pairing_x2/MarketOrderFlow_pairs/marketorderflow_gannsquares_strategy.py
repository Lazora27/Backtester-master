import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und GannSquares
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'GannSquares': 1.0
        })
    )
