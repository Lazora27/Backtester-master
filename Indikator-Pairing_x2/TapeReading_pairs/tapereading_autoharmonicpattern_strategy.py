import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
