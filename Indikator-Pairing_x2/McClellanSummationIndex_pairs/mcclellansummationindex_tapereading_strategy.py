import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und TapeReading
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'TapeReading': 1.0
        })
    )
