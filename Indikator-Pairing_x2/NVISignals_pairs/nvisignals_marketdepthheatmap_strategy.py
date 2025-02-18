import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
