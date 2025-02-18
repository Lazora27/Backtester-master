import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'AccelerationBands': 1.0
        })
    )
