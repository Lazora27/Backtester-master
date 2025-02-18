import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'PhaseDivergence': 1.0
        })
    )
