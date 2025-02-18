import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
