import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und PivotPoints
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'PivotPoints': 1.0
        })
    )
