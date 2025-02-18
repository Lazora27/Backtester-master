import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
