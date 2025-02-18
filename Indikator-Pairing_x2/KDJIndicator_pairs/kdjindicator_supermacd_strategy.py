import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und SuperMACD
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'SuperMACD': 1.0
        })
    )
