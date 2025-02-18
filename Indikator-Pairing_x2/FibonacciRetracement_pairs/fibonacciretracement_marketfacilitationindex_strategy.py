import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
