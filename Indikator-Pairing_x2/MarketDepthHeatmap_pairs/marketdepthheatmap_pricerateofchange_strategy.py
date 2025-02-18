import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
