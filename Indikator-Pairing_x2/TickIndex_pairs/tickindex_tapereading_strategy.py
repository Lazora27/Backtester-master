import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und TapeReading
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'TapeReading': 1.0
        })
    )
