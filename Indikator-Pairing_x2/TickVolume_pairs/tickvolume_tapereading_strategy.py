import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und TapeReading
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'TapeReading': 1.0
        })
    )
