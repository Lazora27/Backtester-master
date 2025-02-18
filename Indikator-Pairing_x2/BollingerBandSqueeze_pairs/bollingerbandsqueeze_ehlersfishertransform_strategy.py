import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
