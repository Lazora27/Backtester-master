import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'EaseOfMovement': 1.0
        })
    )
