import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
