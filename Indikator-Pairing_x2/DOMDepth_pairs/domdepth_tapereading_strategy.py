import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und TapeReading
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'TapeReading': 1.0
        })
    )
