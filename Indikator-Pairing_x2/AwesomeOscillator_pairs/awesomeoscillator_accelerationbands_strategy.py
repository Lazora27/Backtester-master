import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'AccelerationBands': 1.0
        })
    )
