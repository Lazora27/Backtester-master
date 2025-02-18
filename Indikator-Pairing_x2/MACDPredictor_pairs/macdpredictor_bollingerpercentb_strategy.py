import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'BollingerPercentB': 1.0
        })
    )
