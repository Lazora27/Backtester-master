import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'SmoothedCycle': 1.0
        })
    )
