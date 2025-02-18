import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
