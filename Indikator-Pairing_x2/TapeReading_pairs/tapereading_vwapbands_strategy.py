import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und VWAPBands
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'VWAPBands': 1.0
        })
    )
