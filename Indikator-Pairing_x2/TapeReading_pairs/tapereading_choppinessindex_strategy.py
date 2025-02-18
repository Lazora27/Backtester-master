import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
