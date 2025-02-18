import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'AverageLogRange': 1.0
        })
    )
