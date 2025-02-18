import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und TrendCycles
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'TrendCycles': 1.0
        })
    )
