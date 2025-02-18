import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
