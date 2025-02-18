import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
