import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und TapeReading
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'TapeReading': 1.0
        })
    )
