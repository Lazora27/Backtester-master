import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'GannSquareReversal': 1.0
        })
    )
