import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
