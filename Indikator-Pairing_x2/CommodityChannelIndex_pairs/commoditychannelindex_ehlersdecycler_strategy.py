import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
