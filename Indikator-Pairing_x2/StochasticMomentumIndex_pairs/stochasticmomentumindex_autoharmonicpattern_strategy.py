import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
