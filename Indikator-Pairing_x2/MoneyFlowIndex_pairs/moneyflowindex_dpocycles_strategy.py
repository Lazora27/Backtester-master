import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
