import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'AverageLogRange': 1.0
        })
    )
