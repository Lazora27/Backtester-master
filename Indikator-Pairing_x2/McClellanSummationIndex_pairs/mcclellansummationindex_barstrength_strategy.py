import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'BarStrength': 1.0
        })
    )
