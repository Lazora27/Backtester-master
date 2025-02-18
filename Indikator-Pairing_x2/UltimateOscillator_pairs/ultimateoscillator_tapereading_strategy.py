import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und TapeReading
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'TapeReading': 1.0
        })
    )
