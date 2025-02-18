import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und CycleFinder
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'CycleFinder': 1.0
        })
    )
