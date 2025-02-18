import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und TrendCycles
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'TrendCycles': 1.0
        })
    )
