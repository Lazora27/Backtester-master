import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
