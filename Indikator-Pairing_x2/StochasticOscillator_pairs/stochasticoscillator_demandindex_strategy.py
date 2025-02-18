import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und DemandIndex
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'DemandIndex': 1.0
        })
    )
