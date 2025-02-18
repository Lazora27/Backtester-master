import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und TrendCycles
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'TrendCycles': 1.0
        })
    )
