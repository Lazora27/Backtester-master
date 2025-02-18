import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
