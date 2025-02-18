import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'OpenInterest': 1.0
        })
    )
