import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'StochasticRSI': 1.0
        })
    )
