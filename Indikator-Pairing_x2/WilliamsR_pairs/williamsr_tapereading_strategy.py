import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und TapeReading
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'TapeReading': 1.0
        })
    )
