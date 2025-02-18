import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'HilbertTrendline': 1.0
        })
    )
