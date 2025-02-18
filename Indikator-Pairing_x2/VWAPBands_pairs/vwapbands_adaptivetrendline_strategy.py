import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
