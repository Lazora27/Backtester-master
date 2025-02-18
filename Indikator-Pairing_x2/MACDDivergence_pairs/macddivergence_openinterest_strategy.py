import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und OpenInterest
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'OpenInterest': 1.0
        })
    )
