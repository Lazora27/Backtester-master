import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'VolumeDelta': 1.0
        })
    )
