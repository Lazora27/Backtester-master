import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
