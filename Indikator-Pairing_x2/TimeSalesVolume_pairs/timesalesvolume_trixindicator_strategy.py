import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'TRIXIndicator': 1.0
        })
    )
