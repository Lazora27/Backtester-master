import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
