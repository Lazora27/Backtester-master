import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'WeightedCycle': 1.0
        })
    )
