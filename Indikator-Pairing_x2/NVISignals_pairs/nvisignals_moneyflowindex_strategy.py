import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
