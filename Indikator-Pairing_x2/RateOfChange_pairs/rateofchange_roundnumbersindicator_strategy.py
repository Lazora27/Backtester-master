import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
