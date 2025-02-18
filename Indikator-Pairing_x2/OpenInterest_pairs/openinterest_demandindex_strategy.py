import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und DemandIndex
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'DemandIndex': 1.0
        })
    )
