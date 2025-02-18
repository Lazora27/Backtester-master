import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'ProjectionBands': 1.0
        })
    )
