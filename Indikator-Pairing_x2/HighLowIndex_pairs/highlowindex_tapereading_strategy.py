import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und TapeReading
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'TapeReading': 1.0
        })
    )
