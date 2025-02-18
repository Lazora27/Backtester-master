import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
