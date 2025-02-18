import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
