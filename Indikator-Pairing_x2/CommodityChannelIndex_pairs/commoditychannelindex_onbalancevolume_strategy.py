import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
