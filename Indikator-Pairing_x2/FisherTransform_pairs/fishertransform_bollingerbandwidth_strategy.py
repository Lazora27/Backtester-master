import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
