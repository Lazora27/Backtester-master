import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und CycleFinder
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'CycleFinder': 1.0
        })
    )
