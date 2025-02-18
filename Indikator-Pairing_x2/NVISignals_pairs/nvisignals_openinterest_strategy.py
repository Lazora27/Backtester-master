import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und OpenInterest
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'OpenInterest': 1.0
        })
    )
