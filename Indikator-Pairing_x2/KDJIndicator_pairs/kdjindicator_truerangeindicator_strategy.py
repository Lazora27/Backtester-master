import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
