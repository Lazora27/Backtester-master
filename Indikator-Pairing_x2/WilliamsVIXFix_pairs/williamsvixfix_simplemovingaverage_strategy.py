import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
