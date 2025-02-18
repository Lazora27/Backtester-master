import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
