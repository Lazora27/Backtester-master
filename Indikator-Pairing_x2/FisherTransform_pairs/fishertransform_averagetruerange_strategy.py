import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'AverageTrueRange': 1.0
        })
    )
