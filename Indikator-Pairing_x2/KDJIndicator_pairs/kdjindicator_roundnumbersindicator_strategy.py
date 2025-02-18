import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
