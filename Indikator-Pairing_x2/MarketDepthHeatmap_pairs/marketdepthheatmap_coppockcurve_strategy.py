import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'CoppockCurve': 1.0
        })
    )
