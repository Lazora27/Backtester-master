import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
