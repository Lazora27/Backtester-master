import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und MovingAverage
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'MovingAverage': 1.0
        })
    )
