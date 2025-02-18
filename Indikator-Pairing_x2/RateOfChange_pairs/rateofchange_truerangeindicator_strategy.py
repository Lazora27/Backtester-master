import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
