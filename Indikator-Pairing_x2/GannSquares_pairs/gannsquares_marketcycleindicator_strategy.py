import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
