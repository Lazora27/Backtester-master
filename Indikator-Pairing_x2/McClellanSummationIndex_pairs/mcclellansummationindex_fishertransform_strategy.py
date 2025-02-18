import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und FisherTransform
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'FisherTransform': 1.0
        })
    )
