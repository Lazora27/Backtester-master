import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'ParabolicSAR': 1.0
        })
    )
