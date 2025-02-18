import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
