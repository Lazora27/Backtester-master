import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
