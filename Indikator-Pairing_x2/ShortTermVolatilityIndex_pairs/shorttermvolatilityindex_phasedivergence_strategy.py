import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ShortTermVolatilityIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ShortTermVolatilityIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ShortTermVolatilityIndex': {
                'class': ShortTermVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ShortTermVolatilityIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ShortTermVolatilityIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
