import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und OpenInterest
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'OpenInterest': 1.0
        })
    )
