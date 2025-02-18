import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_NegativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und NegativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'NegativeVolumeIndex': 1.0
        })
    )
