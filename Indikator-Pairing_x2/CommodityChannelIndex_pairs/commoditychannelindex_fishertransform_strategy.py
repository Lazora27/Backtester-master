import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und FisherTransform
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'FisherTransform': 1.0
        })
    )
