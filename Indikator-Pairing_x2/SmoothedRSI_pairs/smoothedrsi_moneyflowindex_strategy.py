import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
