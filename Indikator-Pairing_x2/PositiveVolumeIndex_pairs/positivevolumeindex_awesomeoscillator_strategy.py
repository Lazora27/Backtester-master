import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_AwesomeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und AwesomeOscillator
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'AwesomeOscillator': 1.0
        })
    )
