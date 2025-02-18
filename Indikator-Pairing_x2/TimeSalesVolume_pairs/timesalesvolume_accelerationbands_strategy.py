import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'AccelerationBands': 1.0
        })
    )
