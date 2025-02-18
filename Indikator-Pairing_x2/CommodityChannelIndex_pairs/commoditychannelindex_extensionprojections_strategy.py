import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'ExtensionProjections': 1.0
        })
    )
