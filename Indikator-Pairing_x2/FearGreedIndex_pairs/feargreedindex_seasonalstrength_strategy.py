import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
