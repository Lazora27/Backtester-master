import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
