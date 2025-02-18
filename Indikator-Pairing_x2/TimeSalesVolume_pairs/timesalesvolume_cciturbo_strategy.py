import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und CCITurbo
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'CCITurbo': 1.0
        })
    )
