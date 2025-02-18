import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und GannAngles
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'GannAngles': 1.0
        })
    )
