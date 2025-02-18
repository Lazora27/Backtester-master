import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'KeltnerChannels': 1.0
        })
    )
