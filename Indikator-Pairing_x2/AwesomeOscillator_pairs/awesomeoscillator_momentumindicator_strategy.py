import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'MomentumIndicator': 1.0
        })
    )
