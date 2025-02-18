import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_VerticalHorizontalFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und VerticalHorizontalFilter
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'VerticalHorizontalFilter': {
                'class': VerticalHorizontalFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VerticalHorizontalFilter'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'VerticalHorizontalFilter': 1.0
        })
    )
