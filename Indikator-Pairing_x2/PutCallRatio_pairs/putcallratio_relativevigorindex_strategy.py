import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
