import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
