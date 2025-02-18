import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'TimeCycle': 1.0
        })
    )
