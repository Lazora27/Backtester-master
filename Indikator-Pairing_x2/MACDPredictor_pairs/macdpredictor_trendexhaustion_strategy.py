import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TrendExhaustion': 1.0
        })
    )
