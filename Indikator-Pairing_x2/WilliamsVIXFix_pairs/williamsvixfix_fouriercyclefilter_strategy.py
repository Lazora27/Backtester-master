import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
