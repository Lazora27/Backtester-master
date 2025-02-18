import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'ExtensionProjections': 1.0
        })
    )
