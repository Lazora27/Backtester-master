import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
