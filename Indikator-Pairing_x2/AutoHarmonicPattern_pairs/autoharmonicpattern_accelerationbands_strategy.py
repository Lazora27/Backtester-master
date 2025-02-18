import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'AccelerationBands': 1.0
        })
    )
