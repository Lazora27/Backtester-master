import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
