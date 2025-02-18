import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und FisherTransform
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'FisherTransform': 1.0
        })
    )
