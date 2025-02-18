import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und GannAngles
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'GannAngles': 1.0
        })
    )
