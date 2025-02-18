import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'AverageLogRange': 1.0
        })
    )
