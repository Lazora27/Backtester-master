import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
