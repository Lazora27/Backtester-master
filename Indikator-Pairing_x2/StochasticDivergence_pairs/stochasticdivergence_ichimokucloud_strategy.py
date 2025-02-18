import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'IchimokuCloud': 1.0
        })
    )
