import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
