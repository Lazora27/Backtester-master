import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
