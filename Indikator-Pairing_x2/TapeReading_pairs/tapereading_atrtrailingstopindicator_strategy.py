import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_ATRTrailingStopIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und ATRTrailingStopIndicator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'ATRTrailingStopIndicator': {
                'class': ATRTrailingStopIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ATRTrailingStopIndicator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'ATRTrailingStopIndicator': 1.0
        })
    )
