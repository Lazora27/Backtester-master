import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
