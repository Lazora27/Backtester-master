import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
