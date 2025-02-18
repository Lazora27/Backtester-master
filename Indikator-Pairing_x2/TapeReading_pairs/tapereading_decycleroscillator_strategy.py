import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
