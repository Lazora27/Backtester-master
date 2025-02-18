import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
