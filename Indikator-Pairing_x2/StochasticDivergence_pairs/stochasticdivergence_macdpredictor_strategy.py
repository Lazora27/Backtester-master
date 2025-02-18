import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'MACDPredictor': 1.0
        })
    )
