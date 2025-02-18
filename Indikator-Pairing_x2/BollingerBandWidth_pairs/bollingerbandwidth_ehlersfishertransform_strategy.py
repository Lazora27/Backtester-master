import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
