import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'KDJIndicator': 1.0
        })
    )
