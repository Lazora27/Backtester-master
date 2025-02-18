import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'AverageTrueRange': 1.0
        })
    )
