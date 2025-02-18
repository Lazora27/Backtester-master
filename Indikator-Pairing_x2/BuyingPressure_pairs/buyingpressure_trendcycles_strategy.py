import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und TrendCycles
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'TrendCycles': 1.0
        })
    )
