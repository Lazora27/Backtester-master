import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
