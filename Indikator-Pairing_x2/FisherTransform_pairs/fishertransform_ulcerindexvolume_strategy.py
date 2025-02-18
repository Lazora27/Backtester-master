import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
