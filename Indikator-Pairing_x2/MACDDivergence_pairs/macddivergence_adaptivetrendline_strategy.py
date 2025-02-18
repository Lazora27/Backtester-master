import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
