import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'UlcerIndex': 1.0
        })
    )
