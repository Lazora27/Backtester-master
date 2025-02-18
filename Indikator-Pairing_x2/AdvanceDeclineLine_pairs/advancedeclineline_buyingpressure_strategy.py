import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'BuyingPressure': 1.0
        })
    )
