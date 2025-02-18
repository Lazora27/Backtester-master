import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
