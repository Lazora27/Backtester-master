import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'EaseOfMovement': 1.0
        })
    )
