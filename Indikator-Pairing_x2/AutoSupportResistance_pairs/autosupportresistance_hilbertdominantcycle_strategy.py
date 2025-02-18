import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
