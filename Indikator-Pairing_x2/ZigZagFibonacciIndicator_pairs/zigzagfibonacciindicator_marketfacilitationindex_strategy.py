import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagFibonacciIndicator_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagFibonacciIndicator und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'ZigZagFibonacciIndicator': {
                'class': ZigZagFibonacciIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagFibonacciIndicator'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'ZigZagFibonacciIndicator': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
