import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'TRIXIndicator': 1.0
        })
    )
