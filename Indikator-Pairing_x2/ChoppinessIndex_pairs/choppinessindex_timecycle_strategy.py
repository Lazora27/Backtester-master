import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
