import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und OpenInterest
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'OpenInterest': 1.0
        })
    )
