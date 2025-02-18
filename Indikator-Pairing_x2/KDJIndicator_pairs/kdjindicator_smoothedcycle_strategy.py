import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'SmoothedCycle': 1.0
        })
    )
