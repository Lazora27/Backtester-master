import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
