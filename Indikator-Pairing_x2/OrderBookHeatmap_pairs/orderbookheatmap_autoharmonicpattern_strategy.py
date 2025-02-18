import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
