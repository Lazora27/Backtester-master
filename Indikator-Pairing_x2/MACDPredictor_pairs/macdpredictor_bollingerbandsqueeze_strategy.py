import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
