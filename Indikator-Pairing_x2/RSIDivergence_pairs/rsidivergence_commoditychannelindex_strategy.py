import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
