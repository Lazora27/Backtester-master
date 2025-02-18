import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und TapeReading
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'TapeReading': 1.0
        })
    )
