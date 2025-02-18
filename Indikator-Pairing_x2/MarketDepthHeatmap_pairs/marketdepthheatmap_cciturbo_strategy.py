import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'CCITurbo': 1.0
        })
    )
