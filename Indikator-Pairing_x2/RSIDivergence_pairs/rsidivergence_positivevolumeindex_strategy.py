import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_PositiveVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und PositiveVolumeIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'PositiveVolumeIndex': 1.0
        })
    )
