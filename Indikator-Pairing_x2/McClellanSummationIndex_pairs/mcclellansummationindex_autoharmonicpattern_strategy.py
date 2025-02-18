import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
