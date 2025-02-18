import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
