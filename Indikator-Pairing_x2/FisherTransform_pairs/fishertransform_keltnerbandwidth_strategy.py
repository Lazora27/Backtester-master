import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
