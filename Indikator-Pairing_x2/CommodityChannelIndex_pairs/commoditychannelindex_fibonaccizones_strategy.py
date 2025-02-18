import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'FibonacciZones': 1.0
        })
    )
