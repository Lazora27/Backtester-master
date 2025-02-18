import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
