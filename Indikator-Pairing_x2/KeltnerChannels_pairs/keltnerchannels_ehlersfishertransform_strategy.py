import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
