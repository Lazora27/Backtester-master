import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
