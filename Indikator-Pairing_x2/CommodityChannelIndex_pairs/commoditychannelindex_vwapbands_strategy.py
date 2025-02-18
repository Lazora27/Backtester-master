import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
