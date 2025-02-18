import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
