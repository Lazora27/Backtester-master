import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'BradleySiderograph': 1.0
        })
    )
