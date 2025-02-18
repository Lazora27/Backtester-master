import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
