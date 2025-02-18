import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
