import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
