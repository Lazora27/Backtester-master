import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und TapeReading
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'TapeReading': 1.0
        })
    )
