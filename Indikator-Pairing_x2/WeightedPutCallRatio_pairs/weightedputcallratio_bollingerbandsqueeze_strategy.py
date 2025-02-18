import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
