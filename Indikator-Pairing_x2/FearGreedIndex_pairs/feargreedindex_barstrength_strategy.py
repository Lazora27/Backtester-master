import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'BarStrength': 1.0
        })
    )
