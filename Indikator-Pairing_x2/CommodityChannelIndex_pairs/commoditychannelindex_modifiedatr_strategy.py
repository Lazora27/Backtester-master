import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'ModifiedATR': 1.0
        })
    )
