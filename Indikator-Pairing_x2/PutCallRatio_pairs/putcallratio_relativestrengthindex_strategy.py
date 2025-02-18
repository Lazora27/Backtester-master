import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
