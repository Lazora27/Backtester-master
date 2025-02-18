import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
