import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
