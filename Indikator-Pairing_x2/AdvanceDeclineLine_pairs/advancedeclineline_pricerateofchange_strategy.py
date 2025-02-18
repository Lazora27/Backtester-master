import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
