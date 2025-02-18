import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
