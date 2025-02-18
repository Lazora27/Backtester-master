import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'AroonIndicator': 1.0
        })
    )
