import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
