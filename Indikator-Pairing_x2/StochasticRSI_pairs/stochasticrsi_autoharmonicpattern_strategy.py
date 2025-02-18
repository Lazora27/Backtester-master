import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
