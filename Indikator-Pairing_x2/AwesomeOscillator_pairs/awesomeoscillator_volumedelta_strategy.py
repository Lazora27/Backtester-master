import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'VolumeDelta': 1.0
        })
    )
