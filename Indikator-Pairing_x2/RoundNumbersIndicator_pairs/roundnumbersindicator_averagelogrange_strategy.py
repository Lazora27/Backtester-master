import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'AverageLogRange': 1.0
        })
    )
