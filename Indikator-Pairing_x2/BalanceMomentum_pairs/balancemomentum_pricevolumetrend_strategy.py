import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
