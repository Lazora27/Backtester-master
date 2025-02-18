import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
