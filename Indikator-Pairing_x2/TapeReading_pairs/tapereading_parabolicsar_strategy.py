import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'ParabolicSAR': 1.0
        })
    )
