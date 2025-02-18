import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'WeightedCycle': 1.0
        })
    )
