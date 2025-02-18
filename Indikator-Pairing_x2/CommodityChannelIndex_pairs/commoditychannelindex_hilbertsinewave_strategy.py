import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
