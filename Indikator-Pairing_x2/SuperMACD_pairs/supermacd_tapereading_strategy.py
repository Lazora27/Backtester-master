import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und TapeReading
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'TapeReading': 1.0
        })
    )
