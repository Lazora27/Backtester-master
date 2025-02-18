import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
