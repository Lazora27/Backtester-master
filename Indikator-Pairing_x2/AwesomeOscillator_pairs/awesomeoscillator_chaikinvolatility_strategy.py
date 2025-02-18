import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
