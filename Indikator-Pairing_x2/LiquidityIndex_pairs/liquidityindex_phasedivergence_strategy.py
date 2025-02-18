import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
