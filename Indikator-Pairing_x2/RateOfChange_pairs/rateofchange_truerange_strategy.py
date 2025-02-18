import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und TrueRange
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'TrueRange': 1.0
        })
    )
