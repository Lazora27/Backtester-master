import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TickVolume
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TickVolume': 1.0
        })
    )
