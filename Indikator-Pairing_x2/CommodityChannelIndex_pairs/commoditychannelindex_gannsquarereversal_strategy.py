import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
