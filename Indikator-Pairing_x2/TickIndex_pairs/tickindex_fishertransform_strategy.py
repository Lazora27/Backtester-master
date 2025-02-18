import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und FisherTransform
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'FisherTransform': 1.0
        })
    )
