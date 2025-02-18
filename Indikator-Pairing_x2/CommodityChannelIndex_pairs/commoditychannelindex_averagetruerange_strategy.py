import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
