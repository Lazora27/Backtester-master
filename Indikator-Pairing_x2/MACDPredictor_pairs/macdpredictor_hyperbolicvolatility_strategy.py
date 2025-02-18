import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
