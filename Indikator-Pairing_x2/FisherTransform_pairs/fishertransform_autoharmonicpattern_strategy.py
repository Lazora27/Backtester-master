import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
