import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'TrueRange': 1.0
        })
    )
