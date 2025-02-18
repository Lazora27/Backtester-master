import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'BarStrength': 1.0
        })
    )
