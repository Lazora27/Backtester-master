import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
