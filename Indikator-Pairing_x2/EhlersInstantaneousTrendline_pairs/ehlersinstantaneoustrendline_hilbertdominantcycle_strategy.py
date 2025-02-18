import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersInstantaneousTrendline_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersInstantaneousTrendline und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'EhlersInstantaneousTrendline': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
