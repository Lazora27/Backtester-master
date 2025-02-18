import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AverageTrueRange': 1.0
        })
    )
