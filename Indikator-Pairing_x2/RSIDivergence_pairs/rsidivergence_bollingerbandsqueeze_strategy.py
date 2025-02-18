import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
