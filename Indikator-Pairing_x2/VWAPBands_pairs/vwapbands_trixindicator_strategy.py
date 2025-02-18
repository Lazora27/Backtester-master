import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'TRIXIndicator': 1.0
        })
    )
