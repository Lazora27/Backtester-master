import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_VerticalHorizontalFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und VerticalHorizontalFilter
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'VerticalHorizontalFilter': {
                'class': VerticalHorizontalFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VerticalHorizontalFilter'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'VerticalHorizontalFilter': 1.0
        })
    )
