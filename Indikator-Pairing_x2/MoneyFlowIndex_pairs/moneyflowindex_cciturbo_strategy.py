import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
