import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'TRIXIndicator': 1.0
        })
    )
