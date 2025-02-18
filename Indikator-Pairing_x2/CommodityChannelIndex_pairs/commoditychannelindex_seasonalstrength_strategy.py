import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
