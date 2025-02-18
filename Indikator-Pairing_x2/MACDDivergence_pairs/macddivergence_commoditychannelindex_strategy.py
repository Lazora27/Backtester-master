import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
