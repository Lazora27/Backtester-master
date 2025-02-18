import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'AverageLogRange': 1.0
        })
    )
