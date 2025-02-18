import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
