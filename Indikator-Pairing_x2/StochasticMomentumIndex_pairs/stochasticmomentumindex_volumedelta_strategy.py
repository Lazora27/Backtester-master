import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'VolumeDelta': 1.0
        })
    )
