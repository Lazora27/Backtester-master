import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_AccumulativeSwingIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und AccumulativeSwingIndex
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'AccumulativeSwingIndex': {
                'class': AccumulativeSwingIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulativeSwingIndex'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'AccumulativeSwingIndex': 1.0
        })
    )
