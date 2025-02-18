import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'BollingerPercentB': 1.0
        })
    )
