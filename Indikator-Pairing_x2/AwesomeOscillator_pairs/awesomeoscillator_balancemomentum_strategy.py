import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'BalanceMomentum': 1.0
        })
    )
