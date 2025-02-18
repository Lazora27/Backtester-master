import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
