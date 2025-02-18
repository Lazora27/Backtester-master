import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
