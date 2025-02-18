import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und TapeReading
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'TapeReading': 1.0
        })
    )
