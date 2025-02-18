import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
