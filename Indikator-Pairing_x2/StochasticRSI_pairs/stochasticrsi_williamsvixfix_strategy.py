import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
