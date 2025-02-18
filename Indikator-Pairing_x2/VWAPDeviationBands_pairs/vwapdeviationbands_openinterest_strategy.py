import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und OpenInterest
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'OpenInterest': 1.0
        })
    )
