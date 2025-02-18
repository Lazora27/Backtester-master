import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
