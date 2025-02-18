import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und RateOfChange
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'RateOfChange': 1.0
        })
    )
