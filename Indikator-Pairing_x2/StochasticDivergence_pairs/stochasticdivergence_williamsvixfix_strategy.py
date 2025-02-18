import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
