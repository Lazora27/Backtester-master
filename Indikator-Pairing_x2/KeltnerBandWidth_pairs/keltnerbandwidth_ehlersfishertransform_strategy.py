import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
