import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und WilliamsR
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'WilliamsR': 1.0
        })
    )
