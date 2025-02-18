import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und GannAngles
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'GannAngles': 1.0
        })
    )
