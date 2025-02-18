import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
