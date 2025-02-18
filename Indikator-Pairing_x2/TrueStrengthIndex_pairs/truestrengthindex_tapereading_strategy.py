import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und TapeReading
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'TapeReading': 1.0
        })
    )
