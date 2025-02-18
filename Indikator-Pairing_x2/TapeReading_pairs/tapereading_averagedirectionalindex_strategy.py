import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
