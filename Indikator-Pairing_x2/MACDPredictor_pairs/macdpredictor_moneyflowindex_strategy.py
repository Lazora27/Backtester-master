import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
