import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
