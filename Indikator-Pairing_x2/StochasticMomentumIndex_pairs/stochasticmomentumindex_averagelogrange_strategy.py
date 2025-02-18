import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
