import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und GannFans
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'GannFans': 1.0
        })
    )
