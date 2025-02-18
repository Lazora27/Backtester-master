import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und PivotPoints
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'PivotPoints': 1.0
        })
    )
