import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'PriceSquawk': 1.0
        })
    )
