import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
