import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ArmsIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ArmsIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ArmsIndex': 1.0
        })
    )
