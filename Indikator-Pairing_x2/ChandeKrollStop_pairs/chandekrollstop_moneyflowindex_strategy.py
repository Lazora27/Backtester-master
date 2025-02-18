import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
