import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
