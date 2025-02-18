import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedTimePrice_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedTimePrice und TrendCycles
    """
    
    params = (
        ('indicators', {
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'PolarizedTimePrice': 1.0,
            'TrendCycles': 1.0
        })
    )
