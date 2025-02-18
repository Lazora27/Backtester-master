import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'HilbertTrendline': 1.0
        })
    )
