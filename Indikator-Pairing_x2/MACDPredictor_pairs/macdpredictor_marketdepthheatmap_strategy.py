import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
