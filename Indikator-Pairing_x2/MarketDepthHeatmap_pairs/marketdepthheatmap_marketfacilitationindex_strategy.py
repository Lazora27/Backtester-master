import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
