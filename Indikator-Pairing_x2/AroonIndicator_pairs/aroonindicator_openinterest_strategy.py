import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'OpenInterest': 1.0
        })
    )
