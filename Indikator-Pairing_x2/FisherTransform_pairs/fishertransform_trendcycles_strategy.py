import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und TrendCycles
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'TrendCycles': 1.0
        })
    )
