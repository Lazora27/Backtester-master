import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'EaseOfMovement': 1.0
        })
    )
