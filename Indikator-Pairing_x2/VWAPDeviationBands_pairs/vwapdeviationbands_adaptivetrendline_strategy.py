import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
