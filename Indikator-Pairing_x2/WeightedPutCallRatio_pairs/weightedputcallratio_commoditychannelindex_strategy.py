import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
