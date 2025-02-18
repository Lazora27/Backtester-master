import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
