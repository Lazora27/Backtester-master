import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'SeasonalStrength': 1.0
        })
    )
