import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
