import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
