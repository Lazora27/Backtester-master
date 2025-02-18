import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und SuperTrend
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'SuperTrend': 1.0
        })
    )
