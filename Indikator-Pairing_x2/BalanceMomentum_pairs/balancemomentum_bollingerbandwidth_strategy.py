import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
