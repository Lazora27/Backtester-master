import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'HistoricalATR': 1.0
        })
    )
