import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
