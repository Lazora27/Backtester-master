import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'OpenInterest': 1.0
        })
    )
