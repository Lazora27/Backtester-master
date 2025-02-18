import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'AverageLogRange': 1.0
        })
    )
