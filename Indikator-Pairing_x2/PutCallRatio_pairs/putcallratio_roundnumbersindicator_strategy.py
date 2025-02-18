import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
