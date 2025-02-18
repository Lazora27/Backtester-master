import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
