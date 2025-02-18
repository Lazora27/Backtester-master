import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicTimePrice_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicTimePrice und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ParabolicTimePrice': 1.0,
            'TrendCycles': 1.0
        })
    )
