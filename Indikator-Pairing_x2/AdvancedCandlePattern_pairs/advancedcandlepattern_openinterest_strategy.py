import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'OpenInterest': 1.0
        })
    )
