import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
