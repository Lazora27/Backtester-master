import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
