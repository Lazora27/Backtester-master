import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_VWAPTimeCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und VWAPTimeCycleIndicator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'VWAPTimeCycleIndicator': {
                'class': VWAPTimeCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPTimeCycleIndicator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'VWAPTimeCycleIndicator': 1.0
        })
    )
