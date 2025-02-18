import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und CCITurbo
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'CCITurbo': 1.0
        })
    )
