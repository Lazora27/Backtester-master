import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
