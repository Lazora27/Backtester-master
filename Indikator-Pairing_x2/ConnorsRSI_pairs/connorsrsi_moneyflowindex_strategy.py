import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
