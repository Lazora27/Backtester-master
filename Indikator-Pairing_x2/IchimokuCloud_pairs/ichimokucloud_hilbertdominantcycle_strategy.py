import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
