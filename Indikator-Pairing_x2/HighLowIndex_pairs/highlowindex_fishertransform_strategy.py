import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und FisherTransform
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'FisherTransform': 1.0
        })
    )
