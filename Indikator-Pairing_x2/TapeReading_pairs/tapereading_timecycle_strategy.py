import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und TimeCycle
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'TimeCycle': 1.0
        })
    )
