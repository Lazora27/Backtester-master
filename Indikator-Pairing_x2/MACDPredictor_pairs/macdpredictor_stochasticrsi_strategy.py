import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'StochasticRSI': 1.0
        })
    )
