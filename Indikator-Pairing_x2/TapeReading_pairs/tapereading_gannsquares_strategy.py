import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und GannSquares
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'GannSquares': 1.0
        })
    )
