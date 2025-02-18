import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
