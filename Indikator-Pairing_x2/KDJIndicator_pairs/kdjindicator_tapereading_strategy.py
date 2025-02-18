import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und TapeReading
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'TapeReading': 1.0
        })
    )
