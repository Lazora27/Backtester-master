import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
