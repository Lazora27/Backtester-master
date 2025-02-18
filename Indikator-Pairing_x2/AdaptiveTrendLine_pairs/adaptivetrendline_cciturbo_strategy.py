import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'CCITurbo': 1.0
        })
    )
