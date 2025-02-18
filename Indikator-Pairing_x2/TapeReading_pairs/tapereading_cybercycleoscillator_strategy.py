import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
