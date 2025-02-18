import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'WeeklyCycle': 1.0
        })
    )
