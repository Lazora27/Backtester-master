import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VerticalHorizontalFilter_TTMSqueezeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VerticalHorizontalFilter und TTMSqueezeIndicator
    """
    
    params = (
        ('indicators', {
            'VerticalHorizontalFilter': {
                'class': VerticalHorizontalFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VerticalHorizontalFilter'>
            },
            'TTMSqueezeIndicator': {
                'class': TTMSqueezeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TTMSqueezeIndicator'>
            }
        }),
        ('weights', {
            'VerticalHorizontalFilter': 1.0,
            'TTMSqueezeIndicator': 1.0
        })
    )
